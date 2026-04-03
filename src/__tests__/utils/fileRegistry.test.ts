import { describe, it, expect } from 'vitest'
import { resolveFilePath, getDirFromPath, NAV_SECTIONS } from '../../utils/fileRegistry'

describe('resolveFilePath', () => {
  it('returns absolute paths as-is', () => {
    expect(resolveFilePath('/docs/foo.md', '/docs')).toBe('/docs/foo.md')
  })

  it('resolves relative path against currentDir', () => {
    expect(resolveFilePath('bar.md', '/docs/complexity')).toBe('/docs/complexity/bar.md')
  })

  it('resolves .. segments correctly', () => {
    expect(resolveFilePath('../algorithms/sort.py', '/docs/complexity')).toBe('/docs/algorithms/sort.py')
  })

  it('resolves nested relative path', () => {
    expect(resolveFilePath('sub/file.md', '/docs')).toBe('/docs/sub/file.md')
  })

  it('handles root currentDir', () => {
    expect(resolveFilePath('index.md', '/')).toBe('/index.md')
  })

  it('collapses extra slashes via empty parts', () => {
    expect(resolveFilePath('foo.md', '/docs/a')).toBe('/docs/a/foo.md')
  })
})

describe('getDirFromPath', () => {
  it('returns the directory portion of a path', () => {
    expect(getDirFromPath('/docs/complexity/big-o.md')).toBe('/docs/complexity')
  })

  it('returns / for a top-level file', () => {
    expect(getDirFromPath('/index.md')).toBe('/')
  })

  it('returns the parent for a nested path', () => {
    expect(getDirFromPath('/docs/algorithms/sort.py')).toBe('/docs/algorithms')
  })
})

describe('NAV_SECTIONS', () => {
  it('is a non-empty array', () => {
    expect(Array.isArray(NAV_SECTIONS)).toBe(true)
    expect(NAV_SECTIONS.length).toBeGreaterThan(0)
  })

  it('every section has slug, label, and indexPath', () => {
    for (const section of NAV_SECTIONS) {
      expect(typeof section.slug).toBe('string')
      expect(typeof section.label).toBe('string')
      expect(typeof section.indexPath).toBe('string')
      expect(section.indexPath.startsWith('/docs/')).toBe(true)
      expect(section.indexPath.endsWith('/index.md')).toBe(true)
    }
  })

  it('slugs are unique', () => {
    const slugs = NAV_SECTIONS.map((s) => s.slug)
    expect(new Set(slugs).size).toBe(slugs.length)
  })
})
