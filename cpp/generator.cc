#include <concepts>
#include <coroutine>
#include <exception>

template<typename T>
struct Generator {
  struct promise_type;
  using handle_type = std::coroutine_handle<promise_type>;
  struct iterator;



  struct promise_type {
    T value_;
    std::exception_ptr exception_;

    Generator get_return_object() {
      return Generator(handle_type::from_promise(*this));
    }
    std::suspend_always initial_suspend() { return {}; }
    std::suspend_always final_suspend() noexcept { return {}; }
    void unhandled_exception() { exception_ = std::current_exception(); }
    template<std::convertible_to<T> From> // C++20 concept
    std::suspend_always yield_value(From &&from) {
      value_ = std::forward<From>(from);
      return {};
    }
    void return_void() {}
  };

    class iterator {
        Generator<T> &owner;
        bool done;
        public:
        void advance() {
            owner.h_.resume();
            auto still_going = not owner.h_.done();
            done = not still_going;
        }
        bool operator != (const iterator &r) const {
            return done != r.done;
        }
        iterator(Generator<T> &o, bool d)
        : owner(o), done(d) {
            if ( not done ) advance();
        }
        iterator &operator++() {
            advance();
            return *this;
        }
        T operator*() const {
            return owner.h_.promise().current_value;
        }
    };  

  handle_type h_;

  Generator(handle_type h) : h_(h) {}
  ~Generator() { h_.destroy(); }
  explicit operator bool() {
    fill();
    return !h_.done();
  }
  T operator()() {
    fill();
    full_ = false;
    return std::move(h_.promise().value_);
  }
  iterator begin() {
        return iterator{*this, false};
    }
    iterator end() {
        return iterator{*this, true};
    }

private:
  bool full_ = false;

  void fill() {
    if (!full_) {
      h_();
      if (h_.promise().exception_)
        std::rethrow_exception(h_.promise().exception_);
      full_ = true;
    }
  }
};