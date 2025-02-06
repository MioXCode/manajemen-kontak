from abc import ABC, abstractmethod


class Contact(ABC):
    def __init__(self, name, nomor):
        self._name = name
        self._nomor = nomor

    @abstractmethod
    def display_contact(self):
        pass

    @abstractmethod
    def update_info(self, **kwargs):
        pass


class PersolanContact(Contact):
    def __init__(self, name, nomor, email, alamat):
        super().__init__(name, nomor)
        self._email = email
        self._alamat = alamat

    def display_contact(self):
        print(
            f"[Pribadi] {self._name}, Nomor: {self._nomor}, Email: {self._email}, Alamat: {self._alamat}"
        )

    def update_info(self, **kwargs):
        if "email" in kwargs:
            self._email = kwargs["email"]

        if "alamat" in kwargs:
            self._alamat = kwargs["alamat"]

        if "nomor" in kwargs:
            self._nomor = kwargs["nomor"]

        print(f"Info: Pembaruan untuk kontak {self._name}")

    def get_email(self):
        return self._email

    def get_alamat(self):
        return self._alamat


class BusinessContact(Contact):
    def __init__(self, name, nomor, perusahaan, pekerjaan):
        super().__init__(name, nomor)
        self._perusahaan = perusahaan
        self._pekerjaan = pekerjaan

    def display_contact(self):
        print(
            f"[Bisnis] {self._name}, Nomor: {self._nomor}, Perusahaan: {self._perusahaan}, Pekerjaan: {self._pekerjaan}"
        )

    def update_info(self, **kwargs):
        if "perusahaan" in kwargs:
            self._perusahaan = kwargs["perusahaan"]

        if "pekerjaan" in kwargs:
            self._pekerjaan = kwargs["pekerjaan"]

        if "nomor" in kwargs:
            self._nomor = kwargs["nomor"]

        print(f"Info: Pembaruan untuk kontak {self._name}")


class ContactManage:
    def __init__(self):
        self._contacts = []

    def add_contact(self, contact: Contact):
        self._contacts.append(contact)
        print(f"Kontak {contact._name} telah di tambahkan")

    def search_contact(self, name: str):
        for contact in self._contacts:
            if contact._name.lower() == name.lower():
                contact.display_contact()
                return contact
        print("Kontak tidak di temukan!")
        return None

    def update_contact(self, name: str, **kwargs):
        contact = self.search_contact(name)
        if contact:
            contact.update_info(**kwargs)

    def show_all(self):
        if not self._contacts:
            print("Tidak ada kontak yg tersedia!")
        else:
            for contact in self._contacts:
                contact.display_contact()


class AdvancedContactManager(ContactManage):
    def search_by_type(self, contact_type: str):
        found = False
        for contact in self._contacts:
            if (
                isinstance(contact, PersolanContact)
                and contact_type.lower() == "pribadi"
            ):
                contact.display_contact()
                found = True
            elif (
                isinstance(contact, BusinessContact)
                and contact_type.lower() == "bisnis"
            ):
                contact.display_contact()
                found = True
        if not found:
            print(f"{contact_type} tidak dapat di temukan!")


if __name__ == "__main__":
    manager = AdvancedContactManager()

    personal = PersolanContact("Niam", "0865738492", "email@mail.com", "Jl. Duat")
    busines = BusinessContact(
        "Adi", "0836482637", "PT. Deetech", "Full Stack Developer"
    )

    manager.add_contact(personal)
    manager.add_contact(busines)

    print("\n--- Semua Kontak ---")
    manager.show_all()

    print("\n--- Pencarian Kontak ---")
    manager.search_contact("Verdi")

    print("\n--- Pembaruan Kontak ---")
    manager.update_contact("Niam", email="example@gmail.com")
    manager.update_contact("Adi", nomor="0836425637")

    print("\n--- Seluruh Kontak Setelah Pembaruan ---")
    manager.show_all()

    print("\n--- Pencarian Berdasarkan Type --")
    manager.search_by_type("pribadi")
    manager.search_by_type("bisnis")
