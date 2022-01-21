//Funktion schreibt eine SVG Anweisung auf die Konsole, welche einen Stern erstellt
void svgStar(int x, int y, int edges, int outerRadius)
{
  int innerRadius = outerRadius / 3;
  float pi = 3.141;
  float alpha = 2*pi/(edges*2);
  
  int currentX;
  int currentY;
  float currentAlpha = alpha;
  
  String svgPath = "<path d=\"M " + x + " " + (y - outerRadius) + " ";
  
  for (int i = 0; i < edges; i++)
  {
    currentX = round(innerRadius * sin(currentAlpha) + x);
    currentY = round(- innerRadius * cos(currentAlpha) + y);
    
    svgPath = svgPath + "L " + currentX + " " + currentY + " ";
    
    currentAlpha += alpha;
    
    currentX = round(outerRadius * sin(currentAlpha) + x);
    currentY = round(- outerRadius * cos(currentAlpha) + y);
    
    svgPath = svgPath + "L " + currentX + " " + currentY + " ";
    
    currentAlpha += alpha;  
  }
  
  svgPath = svgPath + "z\" />";
  
  println(svgPath); 
}

void setup()
{
  //Funktionsaufruf: Stern an Position (500,500) mit 8 Ecken und dem Radius 100 erstellt
  svgStar(500, 500, 8, 100);
}
