from LCSMap import LCSMap

t = LCSMap()
t.insert("Bill assigned role bigquery/admin")
t.insert("Dan assigned role bigquery/viewer")
t.insert("Justin assigned role project/owner")
t.insert("Bill deleted role test/role")

t.to_string()
