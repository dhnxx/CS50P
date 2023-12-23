def main ():

    x = input("File name: ").strip().lower()
    print (extensions(x))

def extensions (n):

    dot = n.rfind(".")
    extract = n[dot:].replace(".","")

    match extract:
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "gif" | "png":
            return "image/" + extract
        case "zip":
            return "application/zip"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case _:
            return "application/octet-stream"


main ()
