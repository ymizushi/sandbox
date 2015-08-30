var gulp = require('gulp');
var watch = require('gulp-watch');
var ts = require('gulp-typescript');
var merge = require('merge2');

gulp.task('default', function() {
  var tsResult = gulp.src(['lib/**/*.ts'])
                     .pipe(ts());
  
  return merge([
      tsResult.dts.pipe(gulp.dest('release/definitions')),
      tsResult.js.pipe(gulp.dest('release/js'))
  ]);
});

gulp.task('watch', function () {
  gulp.watch('lib/**/*.ts', ['default']);
});
