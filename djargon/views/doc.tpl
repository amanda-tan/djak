% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>

<p>Documentation goes here.</p>

<html> 
  <head> 
    <script src="jquery.js"></script> 
    <script> 
    $(function(){
      $("#includedContent").load("doc.htm"); 
    });
    </script> 
  </head> 

  <body> 
     <div id="includedContent"></div>
  </body> 
</html>
