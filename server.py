from xmlrpc.server import SimpleXMLRPCServer
import xml.etree.ElementTree as ET

"""def is_even(n):
    return n % 2 == 0"""

def makeNote(topic, note, giventext, ct):
    try:
        print(topic, note, giventext, ct)
        check = ""
        newTopic = ()
        newNote = ()
        newText = ()
        newCT = ()
        for everything in root.findall(".//*[@name='"+ topic +"']/note"):
            check += everything.attrib['name']
            """print(check)
            print(everything.attrib)"""

        if (check == ""): #New Topic
            newTopic = ET.Element('topic', name=topic)
            newNote = ET.SubElement(newTopic, 'note', name=note)
            newText = ET.SubElement(newNote, 'text')
            newText.text = giventext
            newCT = ET.SubElement(newNote, 'timestamp')
            newCT.text = ct
            root.append(newTopic)
            tree.write("db.xml")
            
        else: # Existing topic
            existingTopic = root.find("./*[@name='"+ topic +"']")
            print(existingTopic)
            newNote = ET.SubElement(existingTopic, 'note', name=note)
            newText = ET.SubElement(newNote, 'text')
            newText.text = giventext
            newCT = ET.SubElement(newNote, 'timestamp')
            newCT.text = ct
            tree.write("db.xml")

        return str("Success")
    except:
        return str("Error occured")

def getTopic(topic):

    try:
        Answer = ""

        for everything in root.findall(".//*[@name='"+ topic +"']/note"):
            Answer += "\n" + everything.attrib['name'] + "\n"
            for content in everything.findall(".//"):
                Answer += content.text + "\n"
        
        if (Answer == ""):
            return str("Topic is empty")
        else:
            return str(Answer)
    except:
        return str("Error occured")

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
#server.register_function(is_even, "is_even")
server.register_function(makeNote, "makeNote")
server.register_function(getTopic, "getTopic")

tree = ET.parse('db.xml')
root = tree.getroot()

server.serve_forever()

"""
Heterogenuity: First to reach server gets served first
Openness: Components can be added or replaced
Security: Not secure, e.g. inputs used directly, xmlrpc module is not secure against maliciuosly constructed data
Scalability: Doesn't handle increasing amount of clients as xmlrpc is single-threaded
Failure handling: try-except clauses should keep server alive even if clients fail
If server fails, clients don't have failure handling
Transparency: Distributed nature is hidden from users
"""