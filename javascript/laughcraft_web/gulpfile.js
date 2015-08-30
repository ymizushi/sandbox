var gulp = require('gulp');
var ts = require('gulp-typescript');
var tsc = require('gulp-tsc');
var merge = require('merge2');


gulp.task('default', function() {
    var tsResult = gulp.src(['assets/ts/**/*.ts'])
                       .pipe(ts());
    
    return merge([
        tsResult.dts.pipe(gulp.dest('release/definitions')),
        tsResult.js.pipe(gulp.dest('release/js'))
    ]);
});
