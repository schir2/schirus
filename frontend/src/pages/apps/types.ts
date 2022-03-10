export class FileDirectory {
    files: File[] = []
    directories: Map<string, FileDirectory> = new Map()
}

export function traverseDirectories(entries: FileSystemEntry[]) {
    const directory = new FileDirectory()
    for (const entry of entries) {
        if (entry.isDirectory) {
            // TODO Fix this typing Mess
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            const entryReader = entry.createReader()
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            entryReader.readEntries(entries => {
                directory.directories.set(entry.name, traverseDirectories(entries))
            })

        } else if (entry.isFile) {
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            entry.file(file => {
                directory.files.push(file)
            })
        }
    }
    return directory
}