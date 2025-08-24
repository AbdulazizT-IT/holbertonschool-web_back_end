import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft); // تمرير sqft للـ Building
    this._floors = floors;
  }

  // getter لـ sqft موروث من Building

  // getter لـ floors
  get floors() {
    return this._floors;
  }

  // override للدالة المطلوبة
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
