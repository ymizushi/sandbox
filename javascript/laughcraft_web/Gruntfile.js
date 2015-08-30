module.exports = function(grunt) {
  'use strict';
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    concat: {
      dist: {
        src: [
          'public/javascripts/src/Laugh.js',
          'public/javascripts/src/core/Note.js',
          'public/javascripts/src/core/Score.js',
          'public/javascripts/src/core/ScoreLoader.js',
          'public/javascripts/src/core/JsonObject.js',
          'public/javascripts/src/core/Pianoroll.js',
          'public/javascripts/src/core/Synth.js',
          'public/javascripts/src/main.js'
        ],
        dest: 'public/javascripts/build/laughcraft.js'
      }
    },
 
    uglify: {
      options: {
          banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      build: {
        src: 'public/javascripts/build/laughcraft.js',
        dest: 'public/javascripts/build/laughcraft.min.js'
      }
    },

    watch: {
      files: ['public/javascripts/**/*.js'],
      tasks: ['concat']
    },

    jasmine: {
      dist: {
        src: [
          'public/javascripts/build/laughcraft.js',
        ],
        options: {
          specs: 'spec/*Spec.js',
          helpers: 'spec/*Helper.js'
        }
      }
    }
  });
 
  grunt.loadNpmTasks('grunt-contrib-jasmine');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
 
  grunt.registerTask('build', [ 'concat', 'uglify' ]);
};
