from traits.api import HasTraits, Float, Property, cached_property

class rectangle(HasTraits):
    w = Float(1.0)
    h = Float(2.0)
    area = Property(depends_on=['w', 'h'])

    @cached_property
    def _get_area(self):
        print("computing...")
        return (self.w * self.h)

if __name__ == '__main__':
    r = rectangle()
    r.configure_traits()