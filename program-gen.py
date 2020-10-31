import json
import sys


# Very hack-y. Please don't use! xD


def wrap(content, order):
    border = "border-b border-gray-500"
    bg = "bg-gray-200" if order % 2 == 0 else ""
    class_list = " ".join([bg, border])
    return """<div class="flex flex-col py-3 px-2 """ + class_list + """" style="margin-bottom:0 !important;">
    """ + content + """
    </div>""" 


def presentation(talk, section=None, order=0):
    authors = None
    try:
        authors = talk["authors"]
    except KeyError as e:
        pass
    content = "\n".join([presentation_header(talk["time"], section), presentation_detail(talk, authors, section)])
    return wrap(content, order) 

def break_(talk, section=None, order=0):
    content = "\n".join([presentation_header(talk["time"], talk["title"])])
    return wrap(content, order)


def presentation_header(time, section):
    return """<div class="w-full flex flex-row justify-between">
        """ + presentation_section(time) + """
        """ + presentation_section(section) + """
    </div>"""

def presentation_detail(talk, authors, section):
    author_list = presentation_author_list(talk["authors"]) if authors else ""
    author = ""
    abstract = ""
    if author_list != "":
        author = """<div class="flex flex-col">
            <div class="font-bold">""" + talk["author_type"] + """</div>
            <div class="">
                """ + author_list + """
            </div>
        </div>"""
    if "abstract" in talk:
        abstract = """<div class="flex flex-col">
            <div class="font-bold">Abstract</div>
            <div class="">
                """ + talk["abstract"] + """
            </div>
        </div>"""
    return """
    <div class="flex-grow">
        <div class="flex flex-col">
            """ + presentation_title(talk["title"]) + """
        </div>
        <div class="space-y-2">
        """ + author + """
        """ + abstract + """
        </div>
    </div>"""

def presentation_section(section):
    return f"<span class=\"text-sm uppercase tracking-wide\">{section}</span>"

def presentation_title(title):
    return f"<span class=\"my-4 text-xl font-bold leading-tight\">{title}</span>"

def presentation_author_list(authors):
    class_list = ""
    return f"<span class=\"{class_list}\">" + f", ".join(authors) + "</span>"


def session(session, title, order=0):
    session["title"] = title
    content = "\n".join([presentation_header(session["time"], ""), presentation_detail(session, None, None)])
    return wrap(content, order) 


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Missing argument: program.json")
    program = sys.argv[1]
    print("""Title: Program
    Description: The program for PyHPC 2020 will be available closer to the workshop date.
    URL: program
    Save_as: program/index.html""")
    with open(program) as f:
        j = json.load(f)
        i = 0
        for a in j:
            i += 1
            if a["type"] == "talk":
                print(presentation(a, a["section"], order=i))
            elif a["type"] == "break":
                print(break_(a, order=i))
            elif a["type"] == "session":
                print(session(a, a["section"], order=i))
                for b in a["talks"]:
                    i += 1
                    print(presentation(b, section=a["section"], order=i))
