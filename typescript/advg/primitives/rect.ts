import { Drawable } from './drawable';
import {Point} from './point'
import {Size} from './size'

export class Rect implements Drawable {
    private _start: Point;
    private _size: Size;

    constructor(start: Point, size: Size) {
        this._start = start;
        this._size = size;
    }

    get start(): Point {
        return this._start;
    }
    
    get size(): Size {
        return this._size;
    }
}