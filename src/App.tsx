import type { Component } from 'solid-js'
import type { RouteSectionProps } from '@solidjs/router'
import { Router, Route } from '@solidjs/router'
import Layout from './components/Layout'
import MarkdownRenderer from './components/MarkdownRenderer'
import { fileRegistry } from './utils/fileRegistry'

const HomePage: Component = () => {
  const content = fileRegistry['/index.md'] ?? '# Welcome\n\nNo `index.md` found at project root.'
  return <MarkdownRenderer content={content} currentDir="/" />
}

const SectionPage: Component<RouteSectionProps> = (props) => {
  const section = () => props.params['section'] ?? ''
  const indexPath = () => `/docs/${section()}/index.md`
  const content = () =>
    fileRegistry[indexPath()] ?? `# ${section()}\n\nContent coming soon.`
  return (
    <MarkdownRenderer content={content()} currentDir={`/docs/${section()}`} />
  )
}

const App: Component = () => (
  <Router root={Layout}>
    <Route path="/" component={HomePage} />
    <Route path="/docs/:section" component={SectionPage} />
  </Router>
)

export default App
