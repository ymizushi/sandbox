#!/usr/bin/env ruby

module Rinja
    def self.render(template, values)
        # TODO: openが失敗した時のエラーハンドリングを追加する
        File.open(template, mode="r") do |file|
            r = /(\{\{.*\}\})/ 
            content = file.read
            replace_string_list = []
            content.gsub(r) {
                replace_string = $1
                var = $1.slice(2..-3).gsub(" ", "")
                if values[var.to_sym] then
                    replace_string_list << [replace_string, values[var.to_sym]]
                else
                    replace_string_list << [replace_string, ""]
                end
            }
            
            replace_string_list.each do |l|
                content = content.gsub(l[0], l[1])
            end
            content
        end
    end
end

p Rinja.render("sample.html", hoge:"piyo", fuga:"fuga")
