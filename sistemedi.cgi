#!c:\perl\bin\perl.exe

$rutacss="/styles/";
$rutascr="/cgi-bin/codegen/medicoscaldas/";

use CGI qw(param);
my $paso   = param('p');
my $estilo = param('s');

if($paso == 2)
{
   $regaeditar = param('seleccion');
}
if($paso == 3)
{
   $id=param('nid');
   $nombre=param('nnombre');
   $especialidad=param('nespecialidad');
   $dirfisica=param('ndirfisica');
   $email=param('nemail');
   $celular=param('ncelular');
   $tel=param('ntel');
}
sub mostrarparaeditar
{
   $abrir="datos.dat";
   open(abrir);
   @almacenar=<abrir>;
   close(abrir);
   print "Content-type: text/html\n\n";
   print("<html>");
   print("   <head>");
   print("      <link REL=\"stylesheet\" TYPE=\"text/css\" href='".$rutacss."estilo".$estilo.".css'>");
   print("    </head>\n");
   print("<body>");
   print("   <h2>Paso # 1: Seleccione el registro que desea editar</h2><br>");
   print("   <form action='".$rutascr."sistemedi.cgi' method='post'>\n");
   print("   <table border=1 align='center' width='80%'>");
   print("   <tr>\n");
   print("      <th>X</th>\n");
   print("      <th>id</th>\n");
   print("      <th>nombre</th>\n");
   print("      <th>especialidad</th>\n");
   print("      <th>dirfisica</th>\n");
   print("      <th>email</th>\n");
   print("      <th>celular</th>\n");
   print("      <th>tel</th>\n");
   print("   </tr>\n");
   foreach(@almacenar)    #To know the biggest
   {
      @registro=split(/::/,$_);
      print("<tr>\n");
      print("<td><input type=radio name='seleccion' value='$registro[0]'></td>\n");
      print("<td>$registro[0]</td>\n");
      print("<td>$registro[1]</td>\n");
      print("<td>$registro[2]</td>\n");
      print("<td>$registro[3]</td>\n");
      print("<td>$registro[4]</td>\n");
      print("<td>$registro[5]</td>\n");
      print("<td>$registro[6]</td>\n");
      print("</tr>\n");
   }
   print("</table><br>");
   print("<table align='center' border=0>");
   print("<tr>\n");
   print("   <td><input type='hidden' name='p' value='2'>\n");
   print("       <input type='hidden' name='s' value='2'>\n");
   print("       <input type='submit' value='Editarlo'></td>\n");
   print("   <td><input type='reset' value='Borrar'></td>\n");
   print("</tr>\n");
   print("</table><br>");
   print("</form>");
   print("</body></html>");
}

sub editarlo
{
   $abrir="datos.dat";
   open(abrir);
   @almacenar=<abrir>;
   close(abrir);
   print "Content-type: text/html\n\n";
   print("<html>");
   print("   <head>");
   print("      <link REL=\"stylesheet\" TYPE=\"text/css\" href='".$rutacss."estilo".$estilo.".css'>");
   print("    </head>\n");
   print("<body>");
   print("<h2>Paso#2: edite el registro: ".$regaeditar."</h2><br>");
   print("<form action='".$rutascr."sistemedi.cgi' method='get'>\n");
   print("<table align=center border=0>\n");
   foreach(@almacenar)
   {
      @registro=split(/::/,$_);
      if ($registro[0] eq $regaeditar)
      {
         print("<tr>\n");
         print("   <td>id</td><td><input type='hidden' name='nid' value='$registro[0]'>$registro[0]</td>\n");
         print("</tr>\n");
         print("<tr>\n");
         print("   <td>nombre</td>  <td><input type='text' name='nnombre' size=70 value='$registro[1]'></td>\n");
         print("</tr>\n");
         print("<tr>\n");
         print("   <td>especialidad</td>  <td><input type='text' name='nespecialidad' size=70 value='$registro[2]'></td>\n");
         print("</tr>\n");
         print("<tr>\n");
         print("   <td>dirfisica</td>  <td><input type='text' name='ndirfisica' size=50 value='$registro[3]'></td>\n");
         print("</tr>\n");
         print("<tr>\n");
         print("   <td>email</td>  <td><input type='text' name='nemail' size=70 value='$registro[4]'></td>\n");
         print("</tr>\n");
         print("<tr>\n");
         print("   <td>celular</td>  <td><input type='text' name='ncelular' size=15 value='$registro[5]'></td>\n");
         print("</tr>\n");
         print("<tr>\n");
         print("   <td>tel</td>  <td><input type='text' name='ntel' size=20 value='$registro[6]'></td>\n");
         print("</tr>\n");
      }
   }
   print("</table>\n");
   print("<table align='center' border=0>\n");
   print("   <tr>\n");
   print("      <td><input type='hidden' name='p' value='3'>\n");
   print("          <input type='hidden' name='s' value='2'>\n");
   print("          <input type='submit' value='Grabar cambios'></td>\n");
   print("      <td><input type='reset' value='Borrar'></td>\n");
   print("   </tr>\n");
   print("</table>\n");
   print("</form>\n");
   print("</body>\n</html>\n");
}


sub guardarloeditado
{
   $abrir="datos.dat";
   open(abrir);
   @almacenar=<abrir>;
   close(abrir);
   unlink("datos.dat");
   $FILE="datos.dat";
   open(archivconf,">".$FILE);
   foreach(@almacenar)
   {
      @registro=split(/::/,$_);
      if ($registro[0] eq $id)
      {
   $linea=$id."::".$nombre."::".$especialidad."::".$dirfisica."::".$email."::".$celular."::".$tel."::";
   $linea.="\n";
   @reg=split(/::/,$linea);
      }
      else
      {
         $linea=$_;
      }
      print archivconf ($linea);
   }
   close(archivconf);
   print "Content-type: text/html\n\n";
   print("<html>");
   print("   <head>");
   print("      <link REL=\"stylesheet\" TYPE=\"text/css\" href='".$rutacss."estilo".$estilo.".css'>");
   print("    </head>\n");
   print("<body>");
   print("<h2>Los cambios se han hecho bien a:</h2><br>");
   print("<table align=center border=0>");
   print("<tr><td><b>Id:</b></td><td>$reg[0]</td></tr>");
   print("<tr><td><b>nombre:</b></td><td>$reg[1]</td></tr>");
   print("<tr><td><b>especialidad:</b></td><td>$reg[2]</td></tr>");
   print("<tr><td><b>dirfisica:</b></td><td>$reg[3]</td></tr>");
   print("<tr><td><b>email:</b></td><td>$reg[4]</td></tr>");
   print("<tr><td><b>celular:</b></td><td>$reg[5]</td></tr>");
   print("<tr><td><b>tel:</b></td><td>$reg[6]</td></tr>");
   print("</table>");
   print("</body></html>");
}


sub ediregistros
{
   if($paso == 1)
   {
      mostrarparaeditar();
   }
   if($paso == 2)
   {
      editarlo();
   }
   if($paso == 3)
   {
      guardarloeditado();
   }
}

#Body program
ediregistros();
