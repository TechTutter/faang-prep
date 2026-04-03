import type { Component } from 'solid-js'
import { createMemo } from 'solid-js'
import hljs from 'highlight.js'
import 'highlight.js/styles/github.css'

interface CodeBlockProps {
  code: string
  language: string
  filename?: string
}

const CodeBlock: Component<CodeBlockProps> = (props) => {
  const highlighted = createMemo(() => {
    try {
      return hljs.highlight(props.code.trimEnd(), { language: props.language }).value
    } catch {
      return props.code
        .trimEnd()
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
    }
  })

  return (
    <div class="my-4 rounded-lg overflow-hidden border border-gray-200 font-mono text-sm">
      <div class="flex items-center justify-between px-4 py-2 bg-gray-100 border-b border-gray-200">
        <span class="text-xs text-gray-500 uppercase tracking-widest font-sans">
          {props.filename ?? props.language}
        </span>
      </div>
      <pre class="overflow-x-auto p-4 bg-gray-50 m-0 leading-relaxed">
        <code
          class={`hljs language-${props.language}`}
          innerHTML={highlighted()}
        />
      </pre>
    </div>
  )
}

export default CodeBlock
