h, w, n = gets.chomp.split(' ').map(&:to_i)

def init_filed(h, w)
  (1..h).map do |eh|
    (1..w).map do |ew|
      '.'
    end
  end
end

def create_row(ew, x)
  row = (1..w).map('.')
  row.map do |i|
    if i <= x and x < x+ew
      '#'
    else
      '.'
    end
  end
end

def update_row(a_row, b_row)

end

(1..n).each do |i|
  filed = init_filed(h,w)
  eh,ew,x = gets.chomp.split(' ').map(&:to_i)
  row = create_row(ew,x)
end



