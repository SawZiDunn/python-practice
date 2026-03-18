class Booking:
    def __init__(self, booking_id, hotel_id, checkin, checkout):
        self.booking_id = booking_id
        self.hotel_id = hotel_id
        self.checkin = checkin
        self.checkout = checkout

    def conflicts_with(self, other):
        """Check if this booking overlaps with another booking."""
        return not (self.checkout < other.checkin or self.checkin > other.checkout)

    def __repr__(self):
        return f"  Booking ID: {self.booking_id} | {self.checkin} -> {self.checkout}"


class Hotel:
    def __init__(self, hotel_id, name):
        self.hotel_id = hotel_id
        self.name = name
        self.bookings: list[Booking] = []

    def add_booking(self, booking: Booking) -> bool:
        """Add booking if no date conflict exists. Returns True if successful."""
        for existing in self.bookings:
            if booking.conflicts_with(existing):
                print(f"Date conflict: Hotel '{self.name}' is already booked from "
                      f"{existing.checkin} to {existing.checkout}.")
                return False
        self.bookings.append(booking)
        return True

    def remove_booking(self, booking_id: int) -> bool:
        """Remove booking by ID. Returns True if found and removed."""
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                self.bookings.remove(booking)
                return True
        print(f"Booking ID {booking_id} not found in hotel '{self.name}'.")
        return False

    def __repr__(self):
        if not self.bookings:
            return f"Hotel: {self.name}\n  No current bookings."
        bookings_str = "\n".join(str(b) for b in self.bookings)
        return f"Hotel: {self.name}\n{bookings_str}"


class HotelManager:
    def __init__(self):
        self.hotels: dict[int, Hotel] = {}
        self.bookings: dict[int, Booking] = {}
        self._hotel_id = 1
        self._booking_id = 1

    def create_hotel(self, name: str):
        hotel = Hotel(self._hotel_id, name)
        self.hotels[self._hotel_id] = hotel
        self._hotel_id += 1

    def book_hotel(self, hotel_id: int, checkin: int, checkout: int):
        if not (1 <= checkin <= 365):
            print("Error: Provide a valid check-in date (1-365).")
            return

        if not (1 <= checkout <= 365):
            print("Error: Provide a valid check-out date (1-365).")
            return

        if checkin >= checkout:
            print("Error: Check-in date must be before check-out date.")
            return

        if hotel_id not in self.hotels:
            print(f"Error: Hotel ID {hotel_id} does not exist.")
            return

        booking = Booking(self._booking_id, hotel_id, checkin, checkout)
        success = self.hotels[hotel_id].add_booking(booking)

        if success:
            self.bookings[self._booking_id] = booking
            self._booking_id += 1

    def cancel_booking(self, hotel_id: int, booking_id: int):
        if hotel_id not in self.hotels:
            print(f"Error: Hotel ID {hotel_id} does not exist.")
            return

        success = self.hotels[hotel_id].remove_booking(booking_id)
        if success and booking_id in self.bookings:
            del self.bookings[booking_id]

    def process_command(self, cmd: str):
        parts = cmd.split()

        if parts[0] == "create" and parts[1] == "hotel":
            self.create_hotel(parts[2])

        elif parts[0] == "book":
            self.book_hotel(int(parts[1]), int(parts[2]), int(parts[3]))

        elif parts[0] == "cancel":
            self.cancel_booking(int(parts[1]), int(parts[2]))

        else:
            print(f"Unknown command: {cmd}")

    def print_summary(self):
        print("\n===== Hotel Bookings Summary =====")
        if not self.hotels:
            print("No hotels registered.")
            return
        for hotel in self.hotels.values():
            print(hotel)
            print()


# ── Main ──────────────────────────────────────────────────────────────────────
manager = HotelManager()
n = int(input())

for _ in range(n):
    manager.process_command(input())

manager.print_summary()