import { Canvas } from "./canvas";
import { Drawable } from "./drawable";

export class Point implements Drawable{
    private _x: number;
    private _y: number;

    constructor(x: number, y: number) {
        this._x = x
        this._y = y

    }

    get x(): number {
        return this._x;
    }

    get y(): number {
        return this._y;
    }
}