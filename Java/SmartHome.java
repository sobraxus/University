package IOT_System;

public class SmartHome {

    private SmartPlug[] plugs; //Creates array plugs
    private SmartRoom[] rooms; //Creates array rooms
    private String[] deviceList = {"Lamp", "TV", "Computer", "Phone Recharger", "Heater"}; //String array with pre-defined values for devices
    private int roomIndex;//Creates index for room - can be used to increment
    private int plugIndex;//Creates index for plug - can be used to increment

    public SmartHome(int roomAmount, int plugAmount) {
        plugs = new SmartPlug[plugAmount]; //Sets the size of the plugs array to value entered by user
        rooms = new SmartRoom[roomAmount]; //Sets the size of the rooms array to value entered by user
        roomIndex = 0; //Initiates roomIndex
        plugIndex = 0; //Initiates plugIndex
    }

    public int plugSize() {
        return plugs.length;
    } //Creates method with value of amount of plugs e.g. 4

    public int roomSize() {
        return rooms.length;
    } //Creates method with value of amount of rooms e.g. 2

    public void addRoom(String Name, int ID) {
        if (roomIndex >= roomSize()) {
            return; //If the index becomes larger or equal to roomSize() roomIndex will no longer increment.
        }
        SmartRoom room = new SmartRoom(Name, ID); //Creates room with name entered by user and generated ID
        rooms[roomIndex] = room; //Sets the room to the current place within the array
        roomIndex++; //Increments the Index
    }

    public void addPlug(boolean standardStatus, int roomID, int ID, String name, int device) {
        if (plugIndex >= plugSize()) {
            return;//If the index becomes larger or equal to plugSize() plugIndex will no longer increment.
        }
        SmartPlug plug = new SmartPlug(standardStatus, roomID, ID, name, device); //Creates plug populated with plug and device data
        plugs[plugIndex] = plug;//Sets the plug to the current place within the array
        plugIndex++;//Increments the Index
    }

    public String availableRooms() {
        StringBuilder s = new StringBuilder();
        for (SmartRoom Room : rooms) {
            s.append(Room.roomLst());
        }
        return s.toString();
    }

    public void Display() {
        StringBuilder s = new StringBuilder();//Creates StringBuilder object with variable name s
        s.append("\t\t ************ DASHBOARD ************ ");//Adds string to s
        for (SmartRoom Room : rooms) {//Runs through room array
            s.append("\n ROOM: " + Room.getId()); //Adds "Room: + roomID" to s
            for (SmartPlug Plug : plugs) { //Runs through plug array
                    if (Room.getId() == Plug.getroomID()) { //Sorts plugs to fall under their rooms.
                        s.append(Plug.deviceToString()); //Adds device data to s
                        s.append(Room);//adds room data to s
                        s.append(Plug.plugToString());//adds plug data to s
                    }
                }
        }
        System.out.println(s);//Displays data added to variable s accordingly.
    }


    public void plugsOn() {
        for (SmartPlug plug : plugs) { //Runs through each plug within plugs array
            if (!plug.isStatus()) {//While a plug's status = false
                plug.setStatus(true);//Set the status = true
            }
        }
    }

    public void plugsOff() {
        for (SmartPlug plug : plugs) {//Runs through each plug within plugs array
            if (plug.isStatus()) { //Whilst plug = true
                plug.setStatus(false); //set plug = false
            }
        }
    }

    public void turnRoomOn(int ID) {
        for (SmartPlug plug : plugs) {//Runs through each plug within plugs array
            if (plug.getroomID() == ID) {//Gets the room ID
                plug.setStatus(true);//Sets all plugs within the room to true
            }
        }
    }

    public void turnRoomOff(int ID) {
        for (SmartPlug plug : plugs) {//Runs through each plug within plugs array
            if (plug.getroomID() == ID) { //Gets the room ID
                plug.setStatus(false);//Sets all plugs within the room to false
            }
        }
    }

    public void toggle(int plugID) {
        for (SmartPlug plug : plugs) {//Runs through each plug within plugs array
            if (plug.getId() == plugID) { //If the plug ID entered by the user matches a record
                plug.setStatus(!plug.isStatus());//Sets the status of the plug to the opposite of what it currently is
            }
        }
    }
    public void toggleSingle(int plugID, boolean IO) {
        for (SmartPlug plug : plugs) {//Runs through each plug within plugs array
            if (plug.getId() == plugID) { //If the plug ID entered by the user matches a record
                plug.setStatus(IO);//Sets status to either true or false for single plug (IO declared in ConsoleOutput)
            }
        }
    }
    public void changeDevice(int plugID, int newDeviceID){ //Working
        for (SmartPlug plug : plugs) { //Runs through each plug within plugs array
            if(plug.getId() == plugID){ // ID must be equal to ID entered by user
                plug.setDeviceID(newDeviceID); //Sets the device ID to value entered by user
                String name = deviceList[newDeviceID - 1]; //Uses device ID to choose device from device list
                plug.setName(name); //Changes device name
            }
        }
    }

    public void movePlug(int plugID, int newRoomID){ //Working
        for(SmartPlug plug : plugs){//Runs through each plug within plugs array
            if(plug.getId() == plugID){ //If the plug ID entered by the user matches a record
                plug.setRoomID(newRoomID);//Chosen plugs associated roomID will be changed to entered ID
            }
        }
    }

    public void addNewPlug(int room, int deviceID){
        plugs = new SmartPlug[plugSize()+1];//Adds 1 to the array
        String name = deviceList[deviceID - 1]; //Assigns name according to device ID. (-1 as user number start from 1 not 0)

        SmartPlug plug = new SmartPlug(false, room, plugIndex, name, deviceID); //Creates a new plug with data provided
        plugs[plugIndex] = plug; //Sets the current pl
        plugIndex++;
    }
//    public void addPlug(boolean standardStatus, int roomID, int ID, String name, int device) {
//        if (plugIndex >= plugSize()) {
//            return;
//        }
//        SmartPlug plug = new SmartPlug(standardStatus, roomID, ID, name, device);
//        plugs[plugIndex] = plug;
//        plugIndex++;
//    }
    public void addNewDevice(){

    }
    public void addNewRoom(){

    }
}
