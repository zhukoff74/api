class Query:
    @staticmethod
    def get_invoice() -> str:
        """Получить счет"""
        return """
        SELECT
        MAGAZINES.IDDOCDEF AS DOCTYPE,
        SALES_INVOICE.SP1064 AS TR,  -- (P)ТР
        SALES_INVOICE.SP2372 AS UP,  -- (P)Упаковка
        SALES_INVOICE.SP1063 AS KPS,  -- (P)КПС
        CASE LTRIM(RTRIM(SALES_INVOICE.SP1086))  -- (P)ВидТР
            when 'U2' then 'Naiiauaic'
            when 'U3' then 'Aee??aiu a noiio'
            when 'U4' then 'Ioaaeuiui n?aoii'
            when 'U5' then 'Iiea?eaaaony iieoiaoaeai ia?aaic?eeo'
        END AS TRTYPE,
        (SELECT
        SUM(DOC_MNCH_INVOICE.SP1079)  -- (P)Всего
        FROM
        DT1058 AS DOC_MNCH_INVOICE WITH (NOLOCK)  -- Документ (Мн.ч.) ОПРСчет
        WHERE
        DOC_MNCH_INVOICE.IDDOC=%(iddoc)s) AS SUM,
        (SELECT
        SUM(DOC_MNCH_INVOICE_2.SP1131*DOC_MNCH_INVOICE_2.SP1074)  -- SP1131 (P)ЦенаDDP | SP1074 (P)Количество
        FROM
        DT1058 AS DOC_MNCH_INVOICE_2 WITH (NOLOCK)  -- Документ (Мн.ч.) ОПРСчет
        WHERE
        DOC_MNCH_INVOICE_2.IDDOC=%(iddoc)s) AS SUMDDP
        FROM
        DH1058 AS SALES_INVOICE WITH (NOLOCK)  -- Документ ОПРСчет
        INNER JOIN
        _1SJourn AS MAGAZINES WITH (NOLOCK) -- Журналы
        ON
        MAGAZINES.iddoc=SALES_INVOICE.iddoc
        WHERE
        SALES_INVOICE.iddoc=%(iddoc)s
        """