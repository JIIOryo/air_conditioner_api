# air_conditioner_api

air_conditioner_apiは、エアコンを操作するためのAPIサーバです。

# Endpoints

## PUT:/on/cool
<details>
<summary>
detail
</summary>

#### Schema

```json
{
    "cool": {
        "type": "object",
        "properties": {
            "temperature": {
                "type": "number",
                "minimum": 16,
                "maximum": 31,
                "description": "Degree celsius of airflow from air conditioner."
            },
            "airflowLevel": {
                "type": "string",
                "enum": ["a", "1", "2", "3"],
                "description": "Level of airflow from air conditioner. a: auto, 1: low, 2: middle, 3: high"
            }
        },
        "required": [
            "temperature",
            "airflowLevel"
        ],
        "examples": [
            {
                "temperature": 26,
                "airflowLevel": "1"
            }
        ]
    }
}
```

#### Content-Type

`application/json`

#### Example

```json
{
    "temperature": 26,
    "airflowLevel": "1"
}
```

</details>



