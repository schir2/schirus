export class Directory {
    name = ""
    parent: Directory | null = null
    root: Directory | null = null
    entries: Map<string, File | Directory> = new Map()

    constructor(
        name: string | null,
        parent: Directory | null,
    ) {
        if (!name && parent) {
            throw new Error("Cannot create a directory with an unspecified name that has no parent")
        } else if (name && parent) {
            throw new Error("Cannot create a directory without a parent unless it's the root directory. The root directory should have no name specified")
        }
        if (name){
            this.name = ""
        }
        else if (this.isValidDirectoryName(name)) {
            this.name = name
        }
        else {

        }
    }

    isValidDirectoryName(directoryName: string | null): boolean {
        console.info(`Write code to check if ${directoryName} is valid`)
        return !!directoryName

    }

    buildDirectoryFromFileSystemEntry(entries: FileSystemEntry[]) {
        const directory = new Directory()
        for (const entry of entries) {
            if (entry.isDirectory) {
                // TODO Fix this typing Mess
                // eslint-disable-next-line @typescript-eslint/ban-ts-comment
                // @ts-ignore
                const entryReader = entry.createReader()
                // eslint-disable-next-line @typescript-eslint/ban-ts-comment
                // @ts-ignore
                entryReader.readEntries(entries => {
                    directory.entries.set(entry.name, this.buildDirectoryFromFileSystemEntry(entries))
                })

            } else if (entry.isFile) {
                // eslint-disable-next-line @typescript-eslint/ban-ts-comment
                // @ts-ignore
                entry.file(file => {
                    directory.entries.set(file.name, file)
                })
            }
        }
        return directory
    }

    delete(entryName: string) {
        this.entries.delete(entryName)
    }

    copy(entry: File | Directory, path: string) {
        console.info(`Copying ${entry.name} to ${path}`)
    }

    move(entry: File | Directory, path: string) {
        this.copy(entry, path)
        this.delete(entry.name)
    }
}