from main import Catalog, db

if __name__ == '__main__':
    dummy_catalog_list = [
        Catalog(name="Category 1", description="Category 1 - Description"),
        Catalog(name="Category 2", description="Category 2 - Description"),
        Catalog(name="Category 3", description="Category 3 - Description"),
        Catalog(name="Category 4", description="Category 4 - Description"),
        Catalog(name="Category 5", description="Category 5 - Description")
    ]
    db.session.add_all(dummy_catalog_list)
    db.session.commit()

