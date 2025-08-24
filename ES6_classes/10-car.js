// 10-car.js

const cloneSymbol = Symbol('clone'); // تعريف Symbol لنسخ الكائن

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // ميثود لنسخ الكائن
  [cloneSymbol]() {
    const newCar = new this.constructor(this._brand, this._motor, this._color); // استخدم `this.constructor` لضمان استنساخ النوع الصحيح.
    return newCar;
  }

  // ميثود للعودة بالكائن نفسه بعد النسخ
  cloneCar() {
    return this[cloneSymbol](); // استخدم الـ Symbol لنسخ الكائن
  }
}
