import { describe, it, expect, vi } from 'vitest'
import { render } from '@solidjs/testing-library'
import MarkdownRenderer from '../../components/MarkdownRenderer'

vi.mock('../../utils/fileRegistry', () => ({
  fileRegistry: {
    '/docs/snippet.py': 'print("hello")',
    '/docs/note.md': '# Note',
    '/docs/complexity/index.md': '# Complexity',
    '/docs/complexity/big-o.md': '# Big-O',
    '/docs/complexity/space.md': '# Space',
  },
  resolveFilePath: (filename: string, currentDir: string) =>
    filename.startsWith('/') ? filename : `${currentDir}/${filename}`,
  getDirFromPath: (p: string) => {
    const idx = p.lastIndexOf('/')
    return idx <= 0 ? '/' : p.slice(0, idx)
  },
  NAV_SECTIONS: [],
}))

// Silence hljs CSS import inside CodeBlock
vi.mock('highlight.js/styles/github.css', () => ({}))
vi.mock('highlight.js', () => ({
  default: {
    highlight: vi.fn(() => ({ value: 'highlighted' })),
  },
}))

describe('MarkdownRenderer', () => {
  it('renders plain markdown content', () => {
    const { container } = render(() => (
      <MarkdownRenderer content="# Hello World" currentDir="/docs" />
    ))
    expect(container.querySelector('h1')?.textContent).toBe('Hello World')
  })

  it('renders a code embed block for .py files', () => {
    const { container } = render(() => (
      <MarkdownRenderer content="[[snippet.py]]" currentDir="/docs" />
    ))
    expect(container.querySelector('pre')).not.toBeNull()
  })

  it('renders fallback for unknown embed files', () => {
    const { container } = render(() => (
      <MarkdownRenderer content="[[missing.py]]" currentDir="/docs" />
    ))
    expect(container.textContent).toContain('Embed not found')
  })

  it('handles mixed markdown and embed segments', () => {
    const { container } = render(() => (
      <MarkdownRenderer
        content={"# Title\n\n[[snippet.py]]\n\nSome text."}
        currentDir="/docs"
      />
    ))
    expect(container.querySelector('h1')?.textContent).toBe('Title')
    expect(container.querySelector('pre')).not.toBeNull()
    expect(container.textContent).toContain('Some text.')
  })

  it('renders multiple embed blocks', () => {
    const { container } = render(() => (
      <MarkdownRenderer content={"[[snippet.py]]\n[[snippet.py]]"} currentDir="/docs" />
    ))
    expect(container.querySelectorAll('pre').length).toBe(2)
  })

  it('wraps output in markdown-body div', () => {
    const { container } = render(() => (
      <MarkdownRenderer content="text" currentDir="/" />
    ))
    expect(container.querySelector('.markdown-body')).not.toBeNull()
  })

  it('appends subpages section when filePath is an index.md with children', () => {
    const { container } = render(() => (
      <MarkdownRenderer
        content="# Complexity"
        currentDir="/docs/complexity"
        filePath="/docs/complexity/index.md"
      />
    ))
    // getSubpages finds big-o.md and space.md → rendered as a list of links
    expect(container.textContent).toContain('Subpages')
    expect(container.textContent).toContain('Big-o')
    expect(container.textContent).toContain('Space')
  })

  it('does not append subpages section for non-index files', () => {
    const { container } = render(() => (
      <MarkdownRenderer
        content="# Big-O"
        currentDir="/docs/complexity"
        filePath="/docs/complexity/big-o.md"
      />
    ))
    expect(container.textContent).not.toContain('Subpages')
  })

  it('does not append subpages when filePath is omitted', () => {
    const { container } = render(() => (
      <MarkdownRenderer content="# Hello" currentDir="/docs/complexity" />
    ))
    expect(container.textContent).not.toContain('Subpages')
  })

  it('subpage links in the appended section are relative paths', () => {
    const { container } = render(() => (
      <MarkdownRenderer
        content="# Complexity"
        currentDir="/docs/complexity"
        filePath="/docs/complexity/index.md"
      />
    ))
    const links = Array.from(container.querySelectorAll('a')).map((a) => a.getAttribute('href'))
    expect(links).toContain('big-o')
    expect(links).toContain('space')
  })
})
