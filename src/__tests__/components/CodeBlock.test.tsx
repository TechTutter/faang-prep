import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render } from '@solidjs/testing-library'
import CodeBlock from '../../components/CodeBlock'

// Mock hljs to control highlight behavior
vi.mock('highlight.js', () => ({
  default: {
    highlight: vi.fn(() => ({ value: '<span class="hljs-keyword">def</span>' })),
  },
}))

// CSS import is a no-op in vitest
vi.mock('highlight.js/styles/github.css', () => ({}))

describe('CodeBlock', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('renders the highlighted code', () => {
    const { container } = render(() => (
      <CodeBlock code="def foo():" language="python" />
    ))
    const code = container.querySelector('code')
    expect(code).not.toBeNull()
    expect(code!.innerHTML).toContain('hljs-keyword')
  })

  it('shows filename in header when provided', () => {
    const { getByText } = render(() => (
      <CodeBlock code="x = 1" language="python" filename="main.py" />
    ))
    expect(getByText('main.py')).toBeInTheDocument()
  })

  it('shows language in header when filename is omitted', () => {
    const { getByText } = render(() => (
      <CodeBlock code="x = 1" language="python" />
    ))
    expect(getByText('python')).toBeInTheDocument()
  })

  it('falls back to escaped HTML when hljs throws', async () => {
    const hljs = await import('highlight.js')
    vi.mocked(hljs.default.highlight).mockImplementationOnce(() => {
      throw new Error('unsupported language')
    })

    const { container } = render(() => (
      <CodeBlock code="<b>test</b>" language="unknown" />
    ))
    const code = container.querySelector('code')
    expect(code!.innerHTML).toContain('&lt;b&gt;')
    expect(code!.innerHTML).not.toContain('<b>')
  })

  it('renders without error when code has trailing whitespace', () => {
    const { container } = render(() => (
      <CodeBlock code={"hello   \n\n"} language="text" />
    ))
    expect(container.querySelector('pre')).not.toBeNull()
  })
})
