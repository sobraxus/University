package IOT_System;

public class SmartPlug {
        private boolean status; //Creates status variable
        private int roomID; //Creates roomID variable
        private int id; //Creates id variable
        private String name; //Creates name variable
        private int deviceID;//Creates deviceID variable

    public SmartPlug(boolean status, int roomID, int id, String name, int device) {
            this.status = status;//Constructor for Status
            this.id = id;//Constructor for id
            this.roomID = roomID;//Constructor for roomID
            this.name = name;//Constructor for name
            this.deviceID = device;//Constructor for device
        }

        public boolean isStatus() {
            return status;
        }//Gets the current status

        public void setStatus(boolean status) {
            this.status = status;
        } //Sets new status

        public int getId() {
            return id;
        } //Gets current ID

        public void setId(int id) {
            this.id = id;
        } //Sets ID to new ID

        public int getroomID() { return roomID; } //Gets current room ID

        public void setRoomID(int roomID) { this.roomID = roomID; } //Sets new room ID

        public String getName() { return name; } //Gets current device name

        public void setName(String name) { this.name = name; } //Sets new device name

        public int getDeviceID() { return deviceID; } //Gets current device ID

        public void setDeviceID(int deviceID) { this.deviceID = deviceID; } //Sets new device ID

//        public void SB(attachedDevice device, SmartRoom room, SmartPlug plug) {
//
//        StringBuilder s = new StringBuilder();
//        s.append(device.toString()).append(room.toString()).append(plug.toString());
//        System.out.println(s);
//        }

        public String plugToString() {
            return "|ID: " +id + "|Status: " + status+"|"; //Custom toString() method to display ID and Status of plug
        }
        public String deviceToString() {
        return "\nSmartPlug |Attached to: " + name + "\t";//Custom toString() method to display name of device
    }

    }

    class SmartRoom {
        private String roomName; //Creates roomName variable
        private int id; //Creates id variable

        public SmartRoom(String roomName, int id) {
            this.roomName = roomName; //Constructor for roomName
            this.id = id; //Constructor for id
        }

        public String getRoomName() {
            return roomName;
        } //Gets current room name

        public void setRoomName(String roomName) {
            this.roomName = roomName;
        } //Sets new room name

        public int getId() {
            return id;
        } //gets current ID

        public void setId(int id) {
            this.id = id;
        } //Sets new room ID

        @Override
        public String toString() {
            return "|Room: " + roomName;
        } //Overrides system toString() to display room name

        public String roomLst() {
            return "\n | Number: " + id + "| Room: " + roomName + " |";
        } //displays ID and room name
    }