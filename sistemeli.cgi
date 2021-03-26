#!c:\perl\bin\perl.exe

$rutacss="/styles/";
$rutascr="/cgi-bin/codegen/medicoscaldas/";

use CGI qw(param);
my $paso   = param('p');
my $estilo = param('s');

sub mostrarparaeliminar
{
   $abrir="datos.dat";
   open(abrir);
   @almacenar=<abrir>;
   close(abrir);
   print "Content-type: text/html\n\n";
   print("<html>");
   print("<head>");
   print("<link REL=\"stylesheet\" TYPE=\"text/css\" href='".$rutacss."estilo".$estilo.".css'>");
   print("</head>\n");
   print("<body><br>");
   print("<form action='".$rutascr."sistemeli.cgi' method='get'>\n");
   print("<h2>Paso # 1: Seleccione los registros que quiere eliminar</h2><br>");
   print("<table border=1 align='center'>");
   print("<tr align=center>\n");
   print("   <th>X</th>\n");
   print("   <th>nombre</th>\n");
   print("   <th>especialidad</th>\n");
   print("   <th>dirfisica</th>\n");
   print("   <th>email</th>\n");
   print("   <th>celular</th>\n");
   print("   <th>tel</th>\n");
   print("</tr>\n");
   foreach(@almacenar)
   {
      @registro=split(/::/,$_);
      print("<tr>\n");
      print("   <td><input type=checkbox name='b$registro[0]' value='$registro[0]'></td>\n");
      print("   <td>$registro[1]</td>");
      print("   <td>$registro[2]</td>");
      print("   <td>$registro[3]</td>");
      print("   <td>$registro[4]</td>");
      print("   <td>$registro[5]</td>");
      print("   <td>$registro[6]</td>");
      print("</tr>\n");
   }
   print("<table align='center' border=0>");
   print("<tr>\n");
   print("   <td><input type='hidden' name='p' value=2>\n");
   print("       <input type='hidden' name='s' value='".$estilo."'>\n");
   print("       <input type='submit' value='Eliminarlos'></td>\n");
   print("   <td><input type='reset' value='limpiar'></td>\n");
   print("</tr>\n");
   print("</table><br>\n");
   print("</form>");
   print("</body></html>");
}

sub eliminarlos
{
   $abrir="datos.dat";
   open(abrir);
   @almacenar=<abrir>;
   close(abrir);
   unlink("datos.dat");
   $FILE="datos.dat";
   open(archivconf,">".$FILE);
   print "Content-type: text/html\n\n";
   print("<html>");
   print("<head>");
   print("<link REL=\"stylesheet\" TYPE=\"text/css\" href='".$rutacss."estilo".$estilo.".css'>");
   print("</head>\n");
   print("<body>");
   print("<h2>Se han eliminado los siguientes registros:</h2>\n");
   print("<table>");
   foreach(@almacenar)
   {
      @registro=split(/::/,$_);
      if (param("b$registro[0]"))
      {
         print("<tr>");
         print("   <td>$registro[0]</td>");
         print("   <td>$registro[1]</td>");
         print("   <td>$registro[2]</td>");
         print("   <td>$registro[3]</td>");
         print("   <td>$registro[4]</td>");
         print("   <td>$registro[5]</td>");
         print("   <td>$registro[6]</td>");
         print("<tr>");
      }
      else
      {
         print archivconf ($_);
      }
   }
   print("</table>");
   close(archivconf);
   print("</body></html>");
}
sub eliminarregistros
{
   if($paso == 1)
   {
      mostrarparaeliminar();
   }
   if($paso == 2)
   {
      eliminarlos();
   }
}

eliminarregistros();
