import { describe, it, expect, vi } from 'vitest'
import { render } from '@solidjs/testing-library'
import type { JSX, ParentProps } from 'solid-js'
import Layout from '../../components/Layout'

vi.mock('@solidjs/router', () => ({
  useLocation: () => ({ pathname: '/docs/complexity' }),
  A: (props: ParentProps<{ href: string; class?: string; classList?: Record<string, boolean> }>): JSX.Element =>
    (<a href={props.href}>{props.children}</a>) as JSX.Element,
}))

vi.mock('../../utils/fileRegistry', () => ({
  fileRegistry: {},
  resolveFilePath: vi.fn(),
  getDirFromPath: vi.fn(),
  NAV_SECTIONS: [
    { slug: 'complexity', label: 'Complexity', indexPath: '/docs/complexity/index.md' },
    { slug: 'algorithms', label: 'Algorithms', indexPath: '/docs/algorithms/index.md' },
  ],
}))

describe('Layout', () => {
  it('renders children', () => {
    const { getByText } = render(() => (
      <Layout>
        <p>Page content</p>
      </Layout>
    ))
    expect(getByText('Page content')).toBeInTheDocument()
  })

  it('renders all nav section labels', () => {
    const { getByText } = render(() => <Layout />)
    expect(getByText('Complexity')).toBeInTheDocument()
    expect(getByText('Algorithms')).toBeInTheDocument()
  })

  it('nav links point to correct href', () => {
    const { container } = render(() => <Layout />)
    const links = container.querySelectorAll('nav a[href]')
    const hrefs = Array.from(links).map((a) => a.getAttribute('href'))
    expect(hrefs).toContain('/docs/complexity')
    expect(hrefs).toContain('/docs/algorithms')
  })

  it('renders the site title', () => {
    const { getByText } = render(() => <Layout />)
    expect(getByText('FAANG Prep')).toBeInTheDocument()
  })

  it('renders a sidebar nav element', () => {
    const { container } = render(() => <Layout />)
    expect(container.querySelector('nav')).not.toBeNull()
  })

  it('renders a main element for content', () => {
    const { container } = render(() => <Layout />)
    expect(container.querySelector('main')).not.toBeNull()
  })
})
