// TODO: Mirroring/Rotating to get all possible walks
//       Validate correctness of walks


int gridSize = 40;
Grid grid;
String[] loadedWalks;
ArrayList<Walk> walks;

int currentWalk = 0;

void setup(){
  size(800, 800);
  background(255);
   
  
  loadedWalks = loadStrings("k6_walks.txt");
  
  grid = new Grid(gridSize);
  walks = new ArrayList();
  
  print("Size of walks array: " + loadedWalks.length + '\n');
  printArray(loadedWalks);
  
  for(int i = 4; i < loadedWalks.length; i++){
    print(loadedWalks[i] + '\n');
    if(loadedWalks[i] != ""){
      walks.add(new Walk(loadedWalks[i], grid));
    }
  }
}

void draw(){
  background(255);
  grid.display(); //<>//
  textSize(32);
  text(currentWalk % walks.size(), 2, 30);
  Walk w = walks.get(currentWalk % walks.size());
  w.display();
  
}

void mouseClicked(){
  currentWalk++;
}
