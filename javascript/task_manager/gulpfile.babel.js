import gulp from 'gulp'
import gulpLoadPlugins from 'gulp-load-plugins'

const $ = gulpLoadPlugins()

gulp.task('script', () =>
  gulp.src('src/es6/**/*.js')
    .pipe($.babel())
    .pipe(gulp.dest('dist/js'))
)
