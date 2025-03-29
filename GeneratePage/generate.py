_FINDTOKEN_CONST = "<!-- ADD NEW ELEMENT HERE -->"

def generateMain(title, pageName, linkingToPageName, mainImgSource, contactInfo, caption, text="", logo="data/logo.png", logo_alt ="Logo", findToken=_FINDTOKEN_CONST):
    
    with open("../" + pageName, "w") as f:
        f.write(f"""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<title>{title}</title>
<!-- TemplateEndEditable -->
<link rel="shortcut icon" type="image/jpg" href={logo}>
<style type="text/css">
<!--
.text {{
	font-family: Arial, Helvetica, sans-serif;
	font-size: 9pt;
	font-style: normal;
	font-weight: normal;
	padding-top: 0px;
	padding-right: 0px;
	padding-bottom: 0px;
	padding-left: 0px;
	left: auto;
	top: auto;
	margin-top: 0px;
	padding: 0;
}}
.texet-italique {{
	font-family: Georgia, "Times New Roman", Times, serif;
	font-size: 9pt;
	font-style: italic;
}}
.body {{
  overflow-y: scroll;
}}

-->
</style>
<!-- TemplateBeginEditable name="head" -->
<!-- TemplateEndEditable -->

<style type="text/css">
<!--
a:link {{ color: #000; text-decoration: underline; color:#000}}
a:visited {{text-decoration: underline; color:#000}}
a:active {{text-decoration: none}}
a:hover {{text-decoration: none}}
a:target {{top:-20px;position:relative;z-index:5;}}
-->
</style></head>


<body class="text" style="overflow-y: scroll">
<table width="1288" border="0" align="center" cellpadding="0" cellspacing="20">
  <tbody><tr align="left" valign="top">
    <td width="182" height="210" nowrap="nowrap" style="position:fixed">
	<br>
	<a href="{pageName}"><img src="{logo}" width="102" height="45" alt="{logo_alt}"></a>
      <p>&nbsp;</p>
      <p>{contactInfo}
  <br>

  </p>
    <p></p></td>
    <td width="138" height="210"><a id="{mainImgSource.split('/')[1].split(".png")[0]}"></a></td>
    <td width="362" height="210"><a href="{linkingToPageName}"><img src="{mainImgSource}" width="362" height="210" alt="newoffice"></a></td>
    <td width="405" height="210" class="text"><p class="text">{caption}<br>
	<br>{text}
  </p>      <p>&nbsp;</p></td>
    <td width="81" height="210">&nbsp;</td>
  </tr>

{findToken}

  
</tbody></table>
<p>&nbsp;</p>


</body></html>


""")

def generateLink(id, title, topPageName, linkPage, linkImg, contactInfo, caption, text="", logo="data/logo.png", logo_alt="Logo", crossImg="data/cross.png"):
    with open("../"+linkPage, "w") as f:
        f.write(f"""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!-- saved from url=(0036)https://laucparis.com/newoffice.html -->
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<!-- TemplateBeginEditable name="doctitle" -->
<title>{title}</title>
<!-- TemplateEndEditable -->
<link rel="shortcut icon" type="image/jpg" href="{logo}">
<style type="text/css">
<!--
.text {{
	font-family: Arial, Helvetica, sans-serif;
	font-size: 9pt;
	font-style: normal;
	font-weight: normal;
	padding-top: 0px;
	padding-right: 0px;
	padding-bottom: 0px;
	padding-left: 0px;
	left: auto;
	top: auto;
	margin-top: 0px;
	padding: 0;
}}
.texet-italique {{
	font-family: Georgia, "Times New Roman", Times, serif;
	font-size: 9pt;
	font-style: italic;
}}
-->
</style>
<!-- TemplateBeginEditable name="head" -->
<!-- TemplateEndEditable -->

<style type="text/css">
<!--
a:link {{ color: #000; text-decoration: underline; color:#000}}
a:visited {{text-decoration: underline; color:#000}}
a:active {{text-decoration: none}}
a:hover {{text-decoration: none}}
-->
</style></head>


<body class="text" style="overflow-y: scroll">
<table width="1288" border="0" align="center" cellpadding="0" cellspacing="20">
  <tbody><tr align="left" valign="top">
    <td width="182" height="210" nowrap="nowrap" style="position:fixed">
	<br>
	<a href="{topPageName}"><img src="{logo}" width="102" height="45" alt="{logo_alt}"></a>
      <p>&nbsp;</p>
      <p>{contactInfo}
  </p>
    <p></p></td>
    <td width="138" height="210">&nbsp;</td>
    <td width="787" height="210">&nbsp;</td>
    <td width="5" height="210" class="text"><p class="text">&nbsp;</p></td>
    <td width="56" height="210">&nbsp;</td>
  </tr>
  <tr>
    <td width="182" height="670" align="left" valign="top" nowrap="nowrap">&nbsp;</td>
    <td width="138" height="670" align="left" valign="top"><p class="text">{caption}<br>
	<br> {text}
  </p>
	 </td>
    <td width="787" height="670" align="left" valign="top"><a><img src="{linkImg}" alt="newoffice" width="787" height="670"></a></td>
    <td width="" height="670" align="left" valign="top"></td>
    <td height="210" valign="top" style="position:fixed"><a href="{topPageName}#{id}"><img src="{crossImg}" width="10" height="11" alt="next"></a></td>
	
  </tr>
</tbody></table>

<script type="text/javascript">
  document.onkeyup = KeyCheck;       
 
 function KeyCheck(e)
 {{
    var KeyID = (window.event) ? event.keyCode : e.keyCode;
 
    switch(KeyID)
    {{ 
	   case 27:
       window.location = "{topPageName}#{id}";
       break;
    }}
 }}
</script>

<p>&nbsp;</p>
</body></html>

""")

def addNewtableElement(mainPage, pageName, linkingToPageName, mainImgSource, caption, text="", findToken=_FINDTOKEN_CONST, id=None):

    if id is None: id = mainImgSource.split('/')[1].split(".png")[0]
    newElement = f"""

    <tr>
    <td width="182" height="210" align="left" valign="top" nowrap="nowrap"><a id="uia"></a></td>
    <td width="138" height="210" align="left" valign="top">&nbsp;<a id="{id}"></a></td>
    <td width="362" height="210" align="left" valign="top"><a href="{linkingToPageName}"><img src="{mainImgSource}" alt="" width="362" height="210"></a></td>

    <td width="405" height="210" class="text", align="left" valign="top"><p class="text">{caption}<br>
	<br>{text}
  </p>      <p>&nbsp;</p></td>

    <td height="210">&nbsp;</td>
  </tr>
{findToken}
  """

    contents = None
    with open("../"+mainPage, "r") as f:
        contents = f.read().split("\n")

    index = contents.index(findToken)

    contents[index] = newElement
    
    with open ("../"+mainPage, "w") as f:
        for line in contents:
            f.write(line)


def link(text, to):
    return f'<a href="{to}" target="_blank"> {text} </a>'

def createText(txt):
    return txt.replace("\n", "<br>")


def generatePage():
    topPage = "TopPage.html"
    logo='data/logo.png'
    contactInfo="Max Mustermann <br> t. +41 923 283292393"

    linkPage = "secondPage.html"
    img = "cat"
    generateLink(img, "SecondPage", topPage, linkPage, "data/kittens.png", contactInfo, "SUDDENLY MANY", text="Heellllooo wooorrlldd!!", logo=logo)
    generateMain( "TOPPAGETITLE", topPage, linkPage, f"data/{img}.png", 
                 contactInfo, 
                 "cat", text=createText(f"""Hello World!
                                            this is a new line.
                                            again
                                            {link("is it?", "https://de.wikipedia.org/wiki/Stummelschwanz-Zwergtyrann")}
                                        """), 
                 
                 logo=logo, logo_alt="This is my awesome logo")
    
    
    secondEntryLink = "secondLink.html"
    img = "robot"
    generateLink(img, "SecondLink", topPage, secondEntryLink, "data/robots.png", contactInfo, "NICE GREETING",  text="How about waving back?", logo=logo)
    addNewtableElement(topPage, "SecondEntry!!", secondEntryLink, f"data/{img}.png", "Robo", text="hellu")

    thirdEntryLink = "thirdLink.html"
    img = "sea"
    generateLink(img, "ThirdLink", topPage, thirdEntryLink, "data/cat.png", contactInfo, "OOOH LOOK AT THAT",  text="UIUIUIUIUIUUIUIUIUIIU", logo=logo)
    addNewtableElement(topPage, "THIRD ENTRy", thirdEntryLink, f"data/{img}.png", "Reelaaaaxxxx", text="huilulu")

    fourthLink = "fourthPageLink.html"
    img = "pika"
    generateLink(img, "FourthPage", topPage, fourthLink, 'data/pikas.png', contactInfo, "PIKAAAA!!!", text="", logo=logo, logo_alt="logo")
    addNewtableElement(topPage, "Fourth Entry", fourthLink, f'data/{img}.png', "Pokemania", "pika?")

    for i in range(10):
        link_i = "newLink"+str(i)+".html"
        img = f"img{i}"
        generateLink(img, f"{i}th page", topPage, link_i, "NoImg", contactInfo, f"Caption{i=}", logo=logo)
        addNewtableElement(topPage, f"{i}-th entry", link_i, "/.png", f"{i=} Caption", f"{i}", id=img)


if __name__ == "__main__":
    '''This is a function that generates the page accordingly. Watch out, that each image only appears once, as 
        its name is currently used as an identifier
    '''
    generatePage()


