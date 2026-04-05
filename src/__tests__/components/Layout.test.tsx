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
  fileRegistry: {
    '/docs/complexity/index.md': '# Complexity',
    '/docs/complexity/big-o.md': '# Big-O',
    '/docs/complexity/space.md': '# Space',
  },
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

  it('shows subpage links for the active section', () => {
    // Mocked location is /docs/complexity, which is active.
    // Mock fileRegistry has big-o.md and space.md under /docs/complexity/
    const { container } = render(() => <Layout />)
    const subLinks = Array.from(container.querySelectorAll('nav a[href]')).map((a) =>
      a.getAttribute('href'),
    )
    expect(subLinks).toContain('/docs/complexity/big-o')
    expect(subLinks).toContain('/docs/complexity/space')
  })

  it('does not show subpages for inactive sections', () => {
    // algorithms has no pages in the mocked fileRegistry
    const { container } = render(() => <Layout />)
    const subLinks = Array.from(container.querySelectorAll('nav a[href]')).map((a) =>
      a.getAttribute('href'),
    )
    expect(subLinks).not.toContain('/docs/algorithms/something')
  })

  it('does not include index.md itself as a subpage', () => {
    const { container } = render(() => <Layout />)
    const subLinks = Array.from(container.querySelectorAll('nav a[href]')).map((a) =>
      a.getAttribute('href'),
    )
    expect(subLinks).not.toContain('/docs/complexity/index')
  })

  it('subpage labels are capitalised', () => {
    const { getByText } = render(() => <Layout />)
    expect(getByText('Big-o')).toBeInTheDocument()
    expect(getByText('Space')).toBeInTheDocument()
  })
})
