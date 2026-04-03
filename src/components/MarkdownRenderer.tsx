import type { Component, JSX } from 'solid-js'
import { For } from 'solid-js'
import { marked } from 'marked'
import EmbedBlock from './EmbedBlock'

interface MarkdownRendererProps {
  content: string
  currentDir: string
}

type Segment =
  | { kind: 'markdown'; text: string }
  | { kind: 'embed'; filename: string }

const EMBED_RE = /\[\[([^\]]+)\]\]/g

function parseSegments(content: string): Segment[] {
  const segments: Segment[] = []
  let last = 0
  let match: RegExpExecArray | null
  EMBED_RE.lastIndex = 0

  while ((match = EMBED_RE.exec(content)) !== null) {
    if (match.index > last) {
      segments.push({ kind: 'markdown', text: content.slice(last, match.index) })
    }
    segments.push({ kind: 'embed', filename: match[1].trim() })
    last = EMBED_RE.lastIndex
  }

  if (last < content.length) {
    segments.push({ kind: 'markdown', text: content.slice(last) })
  }

  return segments.length > 0 ? segments : [{ kind: 'markdown', text: content }]
}

function renderMd(text: string): string {
  return marked(text, { async: false }) as string
}

const MarkdownRenderer: Component<MarkdownRendererProps> = (props) => {
  const segments = () => parseSegments(props.content)

  return (
    <div class="markdown-body">
      <For each={segments()}>
        {(seg): JSX.Element => {
          if (seg.kind === 'embed') {
            return (
              <EmbedBlock filename={seg.filename} currentDir={props.currentDir} />
            )
          }
          return (
            <div
              class="prose prose-gray max-w-none"
              innerHTML={renderMd(seg.text)} // eslint-disable-line solid/no-innerhtml
            />
          )
        }}
      </For>
    </div>
  )
}

export default MarkdownRenderer
