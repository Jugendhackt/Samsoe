<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

    <title>index</title>
    <meta name="description" content="" />
    <meta name="author" content="Christoph Oberhofer" />

    <meta name="viewport" content="width=device-width; initial-scale=1.0" />
    <link rel="stylesheet" type="text/css" href="style.css" />

      <!-- Das neueste kompilierte und minimierte CSS -->
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">

      <!-- Optionales Theme -->
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">

      <!-- Das neueste kompilierte und minimierte JavaScript -->
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
  </head>

  <body>
      <header>
          <div class="headline">
              <h1>Sams�</h1>
              <h2>Zeig Deinen CO2 Verbrauch  (Barcode scaner)</h2>
          </div>
      </header>
      <div>
    <section id="container" class="container">
        <h3>Barcode Scannen</h3>
        <p>Mit hilfe dieses tools kannst du ein produckt einscennen und beckommst den einen wert zur�ck der dir sagt wie sch�dlich 
        dieses produckt f�r die umwelt ist 
            </p>
            
        <div class="controls">
            <fieldset class="input-group">
                <button id="btn" class="stop">Absenden</button> 
                <br>
               <form action="http://100.100.218.137:8080/samsoe/indx.jsp">
    			<input id="btn" type="submit" value="Neuer Versuch">
			   </form> 
            </fieldset>
            <br>
            <span style="font-size:50px" id ="co2wert" class="shadow">  </span>
           <!--  -->
            
            
        </div>
      <div id="result_strip"> 
        <ul class="thumbnails"></ul>
        <ul class="collector"></ul>
      </div>
      <div id="interactive" class="viewport"></div>
      
    </section>
          <footer>
        <p>
         Sanms� by : Sebastian Andre und soe
        </p>
      </footer>
 </div>
    <script src="vendor/jquery-1.9.0.min.js" type="text/javascript"></script>
    <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
    <script src="quagga.js" type="text/javascript"></script>
    <script src="live_w_locator.js" type="text/javascript"></script>
  </body>
</html>