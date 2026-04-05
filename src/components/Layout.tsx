import type { ParentComponent } from 'solid-js'
import { For } from 'solid-js'
import { A, useLocation } from '@solidjs/router'
import { NAV_SECTIONS, fileRegistry } from '../utils/fileRegistry'

function getSectionPages(slug: string): string[] {
  const prefix = `/docs/${slug}/`
  return Object.keys(fileRegistry)
    .filter(path => path.startsWith(prefix) && path.endsWith('.md') && !path.endsWith('/index.md'))
    .map(path => path.slice(prefix.length).replace('.md', ''))
    .sort()
}

const Layout: ParentComponent = (props) => {
  const location = useLocation()

  return (
    <div class="flex h-screen bg-white overflow-hidden">
      {/* Sidebar */}
      <nav class="w-56 shrink-0 flex flex-col border-r border-gray-100 overflow-y-auto">
        <div class="px-5 pt-6 pb-4 border-b border-gray-100">
          <A href="/" class="block no-underline">
            <div class="text-sm font-semibold text-gray-900 tracking-tight">FAANG Prep</div>
            <div class="text-xs text-gray-400 mt-0.5">Personal study notes</div>
          </A>
        </div>

        <div class="flex-1 py-4 px-3">
          <div class="text-[10px] font-semibold uppercase tracking-widest text-gray-400 px-2 mb-2">
            Sections
          </div>
          <ul class="space-y-0.5">
            <For each={NAV_SECTIONS}>
              {(section) => {
                const isActive = () =>
                  location.pathname === `/docs/${section.slug}` ||
                  location.pathname.startsWith(`/docs/${section.slug}/`)
                const subpages = getSectionPages(section.slug)
                return (
                  <li>
                    <A
                      href={`/docs/${section.slug}`}
                      class="block px-2 py-1.5 rounded text-sm no-underline transition-colors"
                      classList={{
                        'bg-blue-50 text-blue-700 font-medium': isActive(),
                        'text-gray-600 hover:bg-gray-50 hover:text-gray-900': !isActive(),
                      }}
                    >
                      {section.label}
                    </A>
                    {isActive() && subpages.length > 0 && (
                      <ul class="mt-0.5 ml-2 space-y-0.5 border-l border-gray-100 pl-2">
                        <For each={subpages}>
                          {(page) => {
                            const isSubActive = () =>
                              location.pathname === `/docs/${section.slug}/${page}`
                            return (
                              <li>
                                <A
                                  href={`/docs/${section.slug}/${page}`}
                                  class="block px-2 py-1 rounded text-xs no-underline transition-colors"
                                  classList={{
                                    'text-blue-700 font-medium bg-blue-50': isSubActive(),
                                    'text-gray-500 hover:bg-gray-50 hover:text-gray-700': !isSubActive(),
                                  }}
                                >
                                  {page.charAt(0).toUpperCase() + page.slice(1)}
                                </A>
                              </li>
                            )
                          }}
                        </For>
                      </ul>
                    )}
                  </li>
                )
              }}
            </For>
          </ul>
        </div>

        <div class="px-5 py-4 border-t border-gray-100">
          <div class="text-[10px] text-gray-400">Edit .md files to update</div>
        </div>
      </nav>

      {/* Main content */}
      <main class="flex-1 overflow-y-auto">
        <div class="max-w-3xl mx-auto px-10 py-10">
          {props.children}
        </div>
      </main>
    </div>
  )
}

export default Layout
