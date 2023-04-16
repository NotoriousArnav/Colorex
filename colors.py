import extcolors, uuid
from colormap import rgb2hex

def extract_colors(image) -> dict:
    colors = extcolors.extract_from_path(image) if isinstance(image, str) else extcolors.extract_from_image(image)
    dt = {}
    dt['raw'] = colors
    dt['colors'] = [
            {
                'rgb':f'rgb{x[0]}',
                'name':hex2name(rgb2hex(x[0][0], x[0][1], x[0][2])),
                'occurence':x[1],
                'hex':rgb2hex(x[0][0], x[0][1], x[0][2])
                } 
            for x in colors[0]
            ]
    return dt

def make_css_pallete(inp:dict, writetofile=False, writeto=str(uuid.uuid4())):
    vars = [f"\t--{c['name'].replace(' ', '-').lower()}: {c['rgb']}" for c in inp]
    vars_str = ',\n'.join(vars)
    css = ":root{\n"+vars_str+"\n}"
    if writetofile:
        with open(f"{writeto}.css", 'xt') as f: f.write(css)
    return css

def hex2name(code:str) -> str:
    import requests
    code = code.replace("#", '')
    dt = requests.get(f"https://www.thecolorapi.com/id?hex={code}").json()
    return dt.get("name").get("value")

