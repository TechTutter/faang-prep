import type { Component } from 'solid-js'
import { Show } from 'solid-js'
import { fileRegistry, resolveFilePath, getDirFromPath } from '../utils/fileRegistry'
import CodeBlock from './CodeBlock'
// MarkdownRenderer is imported lazily via a function reference to avoid circular module
// evaluation issues. Both modules are fully initialized before any component renders.
import MarkdownRenderer from './MarkdownRenderer'

interface EmbedBlockProps {
  filename: string
  currentDir: string
}

function getExtension(filename: string): string {
  return filename.split('.').pop()?.toLowerCase() ?? ''
}

const EmbedBlock: Component<EmbedBlockProps> = (props) => {
  const resolvedPath = () => resolveFilePath(props.filename, props.currentDir)
  const content = () => fileRegistry[resolvedPath()]
  const ext = () => getExtension(props.filename)

  return (
    <Show
      when={content() !== undefined}
      fallback={
        <div class="my-3 px-4 py-3 rounded-lg border border-red-200 bg-red-50 text-sm text-red-600 font-mono">
          Embed not found: {props.filename}
        </div>
      }
    >
      <div class="embed-block">
        <Show
          when={ext() === 'py' || ext() === 'js' || ext() === 'ts' || ext() === 'jsx' || ext() === 'tsx'}
          fallback={
            <MarkdownRenderer
              content={content()!}
              currentDir={getDirFromPath(resolvedPath())}
            />
          }
        >
          <CodeBlock
            code={content()!}
            language={ext()}
            filename={props.filename}
          />
        </Show>
      </div>
    </Show>
  )
}

export default EmbedBlock
