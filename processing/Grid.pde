public class Grid{
  int gridStep;
  int numRows;
  int numCols;
  PVector center;
  
  public Grid(int gridStep){
    this.gridStep = gridStep;
    numRows = height / gridStep;
    numCols = width / gridStep;
    center = new PVector(gridStep * (numRows/2), gridStep * (numCols/2));
  }
  
  public void display(){
    stroke(0);
    for(int i = 0; i < width; i += gridSize){
       line(0, i, height, i); 
    }
    for(int i = 0; i < height; i += gridSize){
       line(i, 0, i, width); 
    }
    fill(0);
    circle(center.y, center.x, 25);
  }
}
