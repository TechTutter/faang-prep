// Loads all markdown and Python files from the project at build time via Vite globs.
// Keys are root-relative paths like '/docs/complexity/big-o.md'

const rootMd = import.meta.glob<string>('/index.md', {
  eager: true,
  query: '?raw',
  import: 'default',
})

const docsMd = import.meta.glob<string>('/docs/**/*.md', {
  eager: true,
  query: '?raw',
  import: 'default',
})

const docsPy = import.meta.glob<string>('/docs/**/*.py', {
  eager: true,
  query: '?raw',
  import: 'default',
})

export const fileRegistry: Readonly<Record<string, string>> = {
  ...rootMd,
  ...docsMd,
  ...docsPy,
}

/** Resolve a [[filename]] reference relative to the current directory. */
export function resolveFilePath(filename: string, currentDir: string): string {
  if (filename.startsWith('/')) return filename
  const raw = `${currentDir}/${filename}`
  const parts = raw.split('/')
  const resolved: string[] = []
  for (const part of parts) {
    if (part === '..') resolved.pop()
    else if (part !== '' && part !== '.') resolved.push(part)
  }
  return '/' + resolved.join('/')
}

/** Strip the filename from a path to get its directory. */
export function getDirFromPath(filePath: string): string {
  const idx = filePath.lastIndexOf('/')
  return idx <= 0 ? '/' : filePath.slice(0, idx)
}

export interface NavSection {
  slug: string
  label: string
  indexPath: string
}

export const NAV_SECTIONS: NavSection[] = [
  { slug: 'complexity',      label: 'Complexity',      indexPath: '/docs/complexity/index.md' },
  { slug: 'data-structures', label: 'Data Structures', indexPath: '/docs/data-structures/index.md' },
  { slug: 'algorithms',      label: 'Algorithms',      indexPath: '/docs/algorithms/index.md' },
  { slug: 'patterns',        label: 'Patterns',        indexPath: '/docs/patterns/index.md' },
  { slug: 'oop',             label: 'OOP & Design',    indexPath: '/docs/oop/index.md' },
  { slug: 'system-design',   label: 'System Design',   indexPath: '/docs/system-design/index.md' },
  { slug: 'concurrency',     label: 'Concurrency',     indexPath: '/docs/concurrency/index.md' },
  { slug: 'networking',      label: 'Networking',       indexPath: '/docs/networking/index.md' },
  { slug: 'databases',       label: 'Databases',       indexPath: '/docs/databases/index.md' },
  { slug: 'behavioral',      label: 'Behavioral',      indexPath: '/docs/behavioral/index.md' },
]
