export default class ClassRoom {
    constructor(maxStudentsSize) {
      this._maxStudentsSize = maxStudentsSize;
    }
  }import ClassRoom from './0-classroom';

  export default function initializeRooms() {
    return [new ClassRoom(19), new ClassRoom(20), new ClassRoom(34)];
  }