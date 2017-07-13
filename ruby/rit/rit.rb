#!/usr/bin/env ruby

class Blob
    def initialize
        @hash_file_name = nil
    end

    def add rest, nod
        p "eeror"
    end
end

class Tree
    def initialize
        @blob_map = {}
    end

    def add dir_list node
        head = dir_list[0]
        rest = dir_list.slice(1, dir_list.length)
        if @blob_map.key_exists?(head)
            @blob_map[head].add(rest, node)
        else
            @blob_map[head] = node
        end
    end
end


class Commit
    def initialize
        @tree = nil
        @previous = nil
    end
end

class Staging
    def initialize tree
        @tree = Marshal.load(Marshal.dump(tree))
    end

    def add path
        file_list = path.split("/")
        @tree.add path
    end
end

class Current
    def initialize
        @tree = nil
    end
end



class Rit
    def self.commit

    end

    def self.add path
        Staging
    end

    def self.create_file_system
        


    end
end

case ARGV[0]
when "add" then
    path = ARGV[1]
    Rit.add(path)
when "commit" then
    p "commit"
else
    p "unknown command"
end
