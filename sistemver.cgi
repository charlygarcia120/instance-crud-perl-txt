#!c:\perl\bin\perl.exe

#****************************************************
# date: 29:1:2012 
# time: 1:17:5 
# 
# Developed by 
# 
#     CodeGen v1.0 (Code Automatic Generator)
#                                                     
# don't hesitate to contact me!!!
# 
# Carlos Garcia 
# charlygarcia120.com 
# 
# 
# This comment will no be removed                      
# Este comentario no debe ser removido                 
#****************************************************


$rutacss="/styles/";
$rutascr="/cgi-bin/codegen/medicoscaldas/";

use CGI qw(param);
my $estilo = param('s');

sub mostrarregistros
{
   $abrir="datos.dat";
   open(abrir);
   flock(abrir,2);
   @almacenar=<abrir>;
   flock(abrir,8);
   close(abrir);
   print "Content-type: text/html\n\n";
   print("<html>");
   print("<head>");
   print("<link REL=\"stylesheet\" TYPE=\"text/css\" href='".$rutacss."estilo".$estilo.".css'>");
   print("</head>\n");
   print("<body>");
   print("<h2>Estos son los registros del sistema</h2><br>");
   print("<TABLE border=1 align='center' width='80%'>");   print("<tr>\n");
   print("   <th>Id</th>");
   print("   <th>nombre</th>");
   print("   <th>especialidad</th>");
   print("   <th>dirfisica</th>");
   print("   <th>email</th>");
   print("   <th>celular</th>");
   print("   <th>tel</th>");
   print("</tr>\n");
   foreach(@almacenar)
   {
      @registro=split(/::/,$_);
      print("<tr>\n");
      print("   <td>$registro[0]</td>");
      print("   <td>$registro[1]</td>");
      print("   <td>$registro[2]</td>");
      print("   <td>$registro[3]</td>");
      print("   <td>$registro[4]</td>");
      print("   <td>$registro[5]</td>");
      print("   <td>$registro[6]</td>");
      print("</tr>\n");
   }
   print("</table>");
   print("</body></html>");
}


mostrarregistros();
