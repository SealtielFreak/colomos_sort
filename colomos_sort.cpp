#include <vector>
#include <numeric>
#include <algorithm>

template<typename T>
std::vector<T> colomossort(std::vector<T> elements, std::size_t limit = 16) {
    const std::size_t size = elements.size();
    std::vector<T> min, max;
    
    T m = std::accumulate(elements.begin(), elements.end(), 0) / size;
    
    if(size <= limit) {
        std::sort(elements.begin(), elements.end());
        return elements;
    }
    
    for(auto v: elements) {
        if(v > m) {
            max.push_back(v);
        } else {
            min.push_back(v);
        }
    }
    
    min = colomossort(min, limit);
    max = colomossort(max, limit);
    
    min.insert(min.end(), max.begin(), max.end());
    
    return min;
}
