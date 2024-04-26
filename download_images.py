import requests
import xml.etree.ElementTree as ET
import os


def main():
    print("Downloading document...")
    r = requests.get("https://nool.sgp1.digitaloceanspaces.com/")
    with open("document.xml", "w") as f:
        f.write(r.text)
    tree = ET.parse("document.xml")
    root = tree.getroot()

    for el in root:
        tag = el.tag.split("}")[1]
        if tag == "Contents":
            path = el[0].text
            if path.endswith(".jpeg") or path.endswith(".jpg") or path.endswith(".png"):
                local_path = f"images/{path.split('/')[-1]}"
                if path.startswith("flags/"):
                    local_path = f"flags/{path.split('/')[-1]}"
                if os.path.exists(local_path):
                    print("Skipping file: ", local_path)
                    continue

                url = f"https://nool.sgp1.digitaloceanspaces.com/{path}"
                r = requests.get(url)

                with open(local_path, "wb") as f:
                    f.write(r.content)
                
                print(url)


if __name__ == '__main__':
    main()



# tree = ET.fromstring(r.text)
# root = tree.getroot()

# print(root.tag)

# # for el in root:
# #     print(dir(el))
# #     if el.tag == "Contents":
# #         print(el)