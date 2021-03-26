#!c:\perl\bin\perl.exe

$rutacss="/styles/";
$rutascr="/cgi-bin/codegen/medicoscaldas/";

use CGI qw(param);
my $paso   = param('p');
my $estilo = param('s');

if($paso == 2)
{
   $nombre=param('nnombre');
   $especialidad=param('nespecialidad');
   $dirfisica=param('ndirfisica');
   $email=param('nemail');
   $celular=param('ncelular');
   $tel=param('ntel');
}
sub mostrarformulariodeingreso  #Importante del paso 1
{
   print "Content-type: text/html\n\n";
   print("<html>");
   print("<head>");
   print("<link REL=\"stylesheet\" TYPE=\"text/css\" href='".$rutacss."estilo".$estilo.".css'>");
   print("</head>\n");
   print("<body>\n");
   print("<h2>Desde aqui se ingresa un dato al sistema:</h2><br>\n");
   print("<form action='/cgi-bin/codegen/medicoscaldas/sisteming.cgi' method='get'>\n");
   print("<table border=1>\n");
   print("<tr>\n");
   print("</tr>\n");
   print("   <tr>\n");
   print("      <td>nombre</td>\n");
   print("      <td><input type='text' name='nnombre' size='70' maxlength='70'></td>\n");
   print("   </tr>\n");
   print("   <tr>\n");
   print("      <td>especialidad</td>\n");
   print("      <td><input type='text' name='nespecialidad' size='70' maxlength='70'></td>\n");
   print("   </tr>\n");
   print("   <tr>\n");
   print("      <td>dirfisica</td>\n");
   print("      <td><input type='text' name='ndirfisica' size='50' maxlength='50'></td>\n");
   print("   </tr>\n");
   print("   <tr>\n");
   print("      <td>email</td>\n");
   print("      <td><input type='text' name='nemail' size='70' maxlength='70'></td>\n");
   print("   </tr>\n");
   print("   <tr>\n");
   print("      <td>celular</td>\n");
   print("      <td><input type='text' name='ncelular' size='15' maxlength='15'></td>\n");
   print("   </tr>\n");
   print("   <tr>\n");
   print("      <td>tel</td>\n");
   print("      <td><input type='text' name='ntel' size='20' maxlength='20'></td>\n");
   print("   </tr>\n");
   print("<tr>\n");
   print("   <td><input type='hidden' name='p' value=2>\n");
   print("       <input type='hidden' name='s' value='".$estilo."'>\n");
   print("       <input type='submit' value='enviar informacion'></td>\n");
   print("   <td><input type='reset' value='Borrar'></td>\n");
   print("</tr>\n");
   print("</table>\n");
   print("</form>\n");
   print("</body>\n");
   print("</html>\n");
}
sub guardarregistro
{
   $abrir="datos.dat";
   open(abrir);
   @almacenar=<abrir>;
   close(abrir);
   $num=0;                #Here is the correspondent number
                           #in the new registry
   foreach(@almacenar)    #to know the biggest
   {
      @registro=split(/::/,$_);
      $numero=$registro[0];
      if ($numero>$num)
      {
         $num=$numero;
      }
      $numero++;
   }
   $num++;
   $FILE="datos.dat";
   open(archivconf,">>".$FILE);
   $linea=$num."::".$nombre."::".$especialidad."::".$dirfisica."::".$email."::".$celular."::".$tel."::";
   $linea.="\n";
   print archivconf ($linea);
   close(archivconf);
   print "Content-type: text/html\n\n";
   print("<html>");
   print("<head>");
   print("<link REL=\"stylesheet\" TYPE=\"text/css\" href='".$rutacss."estilo".$estilo.".css'>");
   print("</head>\n");
   print("<body>");
   print("<h2>El registro:</h2><br>");
   print("<table>");
   print("   <tr><td><b>Id<b></td><td>$num</td></tr>");
   print("   <tr><td><b>nombre<b></td><td>$nombre</td></tr>");
   print("   <tr><td><b>especialidad<b></td><td>$especialidad</td></tr>");
   print("   <tr><td><b>dirfisica<b></td><td>$dirfisica</td></tr>");
   print("   <tr><td><b>email<b></td><td>$email</td></tr>");
   print("   <tr><td><b>celular<b></td><td>$celular</td></tr>");
   print("   <tr><td><b>tel<b></td><td>$tel</td></tr>");
   print("</table>");
   print("<h2>ha sido agregado al sistema satisfactoriamente:</h2><br>");
   print("</body></html>");
}

sub ingregistros
{
   if($paso == 1)
   {
      mostrarformulariodeingreso();
   }
   if($paso == 2)
   {
      guardarregistro();
   }
}

ingregistros();
