import { describe, it, expect, vi } from 'vitest'
import { render } from '@solidjs/testing-library'
import EmbedBlock from '../../components/EmbedBlock'

vi.mock('../../utils/fileRegistry', () => ({
  fileRegistry: {
    '/docs/script.py': 'print("hi")',
    '/docs/notes.md': '# Notes',
    '/docs/app.ts': 'const x = 1',
  },
  resolveFilePath: (filename: string, currentDir: string) =>
    filename.startsWith('/') ? filename : `${currentDir}/${filename}`,
  getDirFromPath: (p: string) => {
    const idx = p.lastIndexOf('/')
    return idx <= 0 ? '/' : p.slice(0, idx)
  },
  NAV_SECTIONS: [],
}))

vi.mock('highlight.js/styles/github.css', () => ({}))
vi.mock('highlight.js', () => ({
  default: {
    highlight: vi.fn(() => ({ value: 'highlighted' })),
  },
}))

describe('EmbedBlock', () => {
  it('shows error fallback when file is not in registry', () => {
    const { container } = render(() => (
      <EmbedBlock filename="missing.py" currentDir="/docs" />
    ))
    expect(container.textContent).toContain('Embed not found')
    expect(container.textContent).toContain('missing.py')
  })

  it('renders CodeBlock for .py files', () => {
    const { container } = render(() => (
      <EmbedBlock filename="script.py" currentDir="/docs" />
    ))
    expect(container.querySelector('pre')).not.toBeNull()
  })

  it('renders CodeBlock for .ts files', () => {
    const { container } = render(() => (
      <EmbedBlock filename="app.ts" currentDir="/docs" />
    ))
    expect(container.querySelector('pre')).not.toBeNull()
  })

  it('renders MarkdownRenderer for .md files', () => {
    const { container } = render(() => (
      <EmbedBlock filename="notes.md" currentDir="/docs" />
    ))
    // MarkdownRenderer wraps in markdown-body
    expect(container.querySelector('.markdown-body')).not.toBeNull()
  })

  it('wraps content in embed-block div', () => {
    const { container } = render(() => (
      <EmbedBlock filename="script.py" currentDir="/docs" />
    ))
    expect(container.querySelector('.embed-block')).not.toBeNull()
  })

  it('resolves relative path against currentDir', () => {
    const { container } = render(() => (
      <EmbedBlock filename="script.py" currentDir="/docs" />
    ))
    // If path resolved correctly, file is found (no error fallback)
    expect(container.textContent).not.toContain('Embed not found')
  })
})
