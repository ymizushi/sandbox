import gulp from 'gulp'
import gulpLoadPlugins from 'gulp-load-plugins'

const $ = gulpLoadPlugins()

gulp.task('compile', () =>
  gulp.src('src/es6/**/*.js')
    .pipe($.babel())
    .pipe(gulp.dest('dist/js'))
)

gulp.task('watch', () =>  {
  var path = './src/es6/**/*.js';
  gulp.watch(path).on('change', function(event) {
    const result = gulp.src(path)
      .pipe($.babel())
      .pipe(gulp.dest('dist/js'));
    console.log("compile finished.");
  })
}
)
