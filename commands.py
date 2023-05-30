commands = {
    "ls": """
    The "ls" command works by accessing the file system and retrieving a list of files and directories in the current directory.
By default, it displays the names of files and directories in a simple format.
Adding flags like "-a" or "-l" modifies the output by showing hidden files or providing detailed information about each file and directory, respectively.
The "-h" flag is used to display file sizes in a more human-readable format (e.g., KB, MB, GB).
The "-R" flag enables recursive listing, which means it shows the contents of directories and their subdirectories.
    """,
    "dirb": """
  
DIRB(1)                     General Commands Manual                    DIRB(1)

NAME
       dirb - Web Content Scanner

SYNOPSIS
       dirb <url_base> <url_base> [<wordlist_file(s)>] [options]

DESCRIPTION
       DIRB  IS  a  Web Content Scanner. It looks for existing (and/or hidden)
       Web Objects. It basically works by launching a dictionary basesd attack
       against a web server and analizing the response.

OPTIONS
       -a <agent_string>
                Specify  your  custom  USER_AGENT.   (Default is: "Mozilla/4.0
              (compatible; MSIE 6.0; Windows NT 5.1)")

       -b      Don't squash or merge sequences of /../ or  /./  in  the  given
              URL.

       -c <cookie_string>
               Set a cookie for the HTTP request.

       -E <certificate>
               Use the specified client certificate file.

       -f      Fine tunning of NOT_FOUND (404) detection.

       -H <header_string>
               Add a custom header to the HTTP request.

       -i      Use case-insensitive Search.

       -l      Print "Location" header when found.

       -N <nf_code>
               Ignore responses with this HTTP code.

       -o <output_file>
               Save output to disk.

       -p <proxy[:port]>
               Use this proxy. (Default port is 1080)

       -P <proxy_username:proxy_password>
               Proxy Authentication.

       -r      Don't Search Recursively.

       -R       Interactive  Recursion.  (Ask in which directories you want to
              scan)

       -S      Silent Mode. Don't show tested words. (For dumb terminals)

       -t      Don't force an ending '/' on URLs.

       -u <username:password>
               Username and password to use.

       -v      Show Also Not Existent Pages.

       -w      Don't Stop on WARNING messages.

       -x <extensions_file>
               Amplify search with the extensions on this file.

       -X <extensions>
               Amplify search with this extensions.

       -z <milisecs>
               Amplify search with this extensions.

SEE ALSO
       brain(x)

The Dark Raver                    27/01/2009                           DIRB(1)
  """,
    "nmap": """
    "-p <port range>": Specifies the port(s) to scan. For example, "-p 1-1000" scans ports from 1 to 1000.
    "-sV": Enables version detection, which attempts to determine the version of the services running on open ports.
    "-O": Performs OS detection to identify the operating system of the target host.
    "-A": Enables aggressive scanning, which combines multiple scan techniques like version detection, OS detection, and script scanning.
"<target>": Specifies the target IP address or hostname to scan. For example, "nmap 192.168.0.1" scans the host with the IP address 192.168.0.1.
    """,
    "cd": """
    The "cd" command changes the current working directory in the command-line interface.
You can specify the directory you want to navigate to as an argument after the "cd" command.
For example, "cd Documents" would change the current directory to the "Documents" directory.
Additionally, using ".." as an argument moves up to the parent directory of the current directory.

    """,
    "pwd": """There are no specific flags for the "pwd" command. It simply displays the current working directory.""",
    "netdiscover": """
    "-r <IP range>": Specifies the IP range to scan. For example, "-r 192.168.0.0/24" scans all IP addresses in the range 192.168.0.1 to 192.168.0.254.
"-i <network interface>": Specifies the network interface to use for scanning.
"-p": Enables promiscuous mode, allowing the tool to capture packets on the network more effectively.
"-t <timeout>": Sets the timeout value for packet capturing.
"-F": Enables fast mode, which speeds up the scanning process.
    """,
    "rm": """
    "-r": Removes directories and their contents recursively.
"-f": Forces the removal of files without prompting for confirmation.
"-i": Prompts for confirmation before removing each file.
"<file/directory>": Specifies the file or directory to remove. For example, "rm file.txt" removes the file named "file.txt".
    """,
    "cp": """
    "-r": Copies directories and their contents recursively.
"-i": Prompts for confirmation before overwriting existing files.
"-v": Enables verbose mode, displaying detailed information about the copying process.
"<source>": Specifies the source file or directory to copy.
"<destination>": Specifies the destination directory where the file or directory should be copied.

    """,
    "mv": """
    "-i": Prompts for confirmation before overwriting existing files.
"-v": Enables verbose mode, displaying detailed information about the moving process.
"<source>": Specifies the source file or directory to move.
"<destination>": Specifies the destination directory where the file or directory should be moved.
    """,
    "mkdir": """
    "-p": Creates parent directories if they don't exist.
    "-v": Enables verbose mode, displaying a message for each directory created.
    "<directory>": Specifies the name of the directory to create.
    """,
}
