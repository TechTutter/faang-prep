import type { ParentComponent } from 'solid-js'
import { For } from 'solid-js'
import { A, useLocation } from '@solidjs/router'
import { NAV_SECTIONS } from '../utils/fileRegistry'

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
